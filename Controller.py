from datetime import datetime
from typing import List

import pandas as pd
from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QComboBox, QDoubleSpinBox, QFileDialog, QMessageBox, QWidget

from Data import initialize_data, write_data
from MainWindow import MainWindow
from Measurement import DatastreamMeasurementWorker, MeasurementPoint, SweepMeasurementWorker
from SourceMeter import ConnectSMUWorker, Source, SourceMeter


class Controller(QObject):

    sourcemeters: List[SourceMeter]
    main_window: MainWindow

    ds_data_file_path: str
    sm_data_file_path: str

    sm_data: pd.DataFrame | None
    ds_data: pd.DataFrame | None

    sm_last_run: List[pd.DataFrame]
    ds_last_run: pd.DataFrame

    _widget_enabled_state: dict[QWidget, bool]

    def __init__(self):
        super().__init__()

        # Initialize fields
        self.sourcemeters = []
        self.sm_data = None
        self.ds_data = None
        self.sm_last_run = [initialize_data()]
        self.ds_last_run = initialize_data()
        self.ds_data_file_path = ""
        self.sm_data_file_path = ""
        self._widget_enabled_state = {}

        # Create the user interface
        self.main_window = MainWindow()
        self.main_window.show()

        # Setup the plotes
        self.main_window.setup_plots(self.sm_last_run[-1], self.ds_last_run)

        # === SMU Connection Tab ===
        self.main_window.smu_search.clicked.connect(self.smu_search_clicked)
        self.main_window.smu_connection_list.itemSelectionChanged.connect(self.smu_connection_selection_changed)
        self.main_window.smu_disconnect.clicked.connect(self.smu_disconnect_clicked)
        self.main_window.smu_identify.clicked.connect(self.smu_identify_clicked)

        # === Sweep tab ===
        self.main_window.sm_run_full_measurement.clicked.connect(self.sm_run_measurement)
        self.main_window.sm_run_quick_measurement.clicked.connect(lambda: self.sm_run_measurement(quick_measurement=True))

        self.main_window.sm_save_last_run.clicked.connect(self.sm_save_last_run)

        # self.main_window.sm_plot_1_settings.clicked.connect(self.main_window.sm_plot_smu_1.show_plot_params_dialog)
        # self.main_window.sm_plot_2_settings.clicked.connect(self.main_window.sm_plot_smu_2.show_plot_params_dialog)

        self.main_window.sm_file_output.clicked.connect(self.sm_choose_data_file_path)

        # === Datastream tab ===
        self.main_window.ds_stream.clicked.connect(self.ds_stream_clicked)

        self.main_window.ds_save_last_run.clicked.connect(self.ds_save_last_run)

        # self.main_window.ds_plot_1_settings.clicked.connect(self.main_window.ds_plot_smu_1.show_plot_params_dialog)
        # self.main_window.ds_plot_2_settings.clicked.connect(self.main_window.ds_plot_smu_2.show_plot_params_dialog)

        self.main_window.ds_file_output.clicked.connect(self.ds_choose_data_file_path)

    @Slot()
    def smu_search_clicked(self):
        # Disconnect all currently connected SMUs
        self.disconnect_all_smus()

        # Create the search thread
        self._smu_search_thread = ConnectSMUWorker(self)
        self._smu_search_thread.progress_update.connect(self.main_window.smu_search_progress.setValue)
        self._smu_search_thread.status_update.connect(self.main_window.smu_search_log.appendPlainText)
        self._smu_search_thread.connections_made.connect(self.connect_smus)
        self._smu_search_thread.finished.connect(self.smu_search_finished)

        # Update the search button
        self.main_window.smu_search.setText("Cancel SMU Search")
        self.main_window.smu_search.clicked.disconnect()
        self.main_window.smu_search.clicked.connect(self._smu_search_thread.cancel_search)

        # Disable the connections list
        self.main_window.smu_connections.setDisabled(True)

        # Start the search
        self._smu_search_thread.start()

    @Slot()
    def smu_search_finished(self):
        # Update the search button
        self.main_window.smu_search.setText("Search for SMUs")
        self.main_window.smu_search.clicked.disconnect()
        self.main_window.smu_search.clicked.connect(self.smu_search_clicked)

        # Enable the connections list
        self.main_window.smu_connections.setDisabled(False)

        # Reset the progress bar
        self.main_window.smu_search_progress.reset()

    @Slot()
    def connect_smus(self, smus: List[SourceMeter]):
        # Disconnect any SMUs that may be connected
        self.disconnect_all_smus()
        self.sourcemeters = smus
        self.update_smu_uis()

    @Slot()
    def disconnect_all_smus(self):
        # Make sure to gracefully disconnect SMUs
        for smu in self.sourcemeters:
            smu.disconnect()

        self.sourcemeters = []

        self.update_smu_uis()

    def update_smu_uis(self):
        self.main_window.smu_connection_list.clear()

        # Add the SMU to the connections list
        for smu in self.sourcemeters:
            self.main_window.smu_connection_list.addItem(smu.serial_number)

        combo_box: QComboBox

        for combo_box in self.main_window.findChildren(QComboBox):

            if "smu_select" in combo_box.objectName():
                combo_box.clear()
                combo_box.addItem("Simulated")

                for smu in self.sourcemeters:
                    combo_box.addItem(smu.serial_number)

    def get_smu_from_serial(self, serial: str, allow_simulated=True):
        for smu in self.sourcemeters:
            if smu.serial_number == serial:
                return smu

        if allow_simulated:
            return SourceMeter()

    def get_selected_smu(self):

        if len(self.main_window.smu_connection_list.selectedItems()) == 0:
            return None

        serial = self.main_window.smu_connection_list.selectedItems()[0].text()

        return self.get_smu_from_serial(serial)

    @Slot()
    def smu_connection_selection_changed(self):
        smu = self.get_selected_smu()

        if smu:
            self.main_window.smu_disconnect.setDisabled(False)
            self.main_window.smu_identify.setDisabled(False)
        else:
            self.main_window.smu_disconnect.setDisabled(True)
            self.main_window.smu_identify.setDisabled(True)

    @Slot()
    def smu_disconnect_clicked(self):

        smu = self.get_selected_smu()

        if smu:
            smu.disconnect()
            self.sourcemeters.remove(smu)
            self.update_smu_uis()

    @Slot()
    def smu_identify_clicked(self):
        smu = self.get_selected_smu()

        if smu:
            smu.beep(1000, 0.5)

    def sm_get_smu_1_source(self):
        return Source.VOLTAGE if self.main_window.sm_voltage_1.isChecked() else Source.CURRENT

    def sm_get_smu_2_source(self):
        return Source.VOLTAGE if self.main_window.sm_voltage_2.isChecked() else Source.CURRENT

    def ds_get_smu_1_source(self):
        return Source.VOLTAGE if self.main_window.ds_voltage_1.isChecked() else Source.CURRENT

    def ds_get_smu_2_source(self):
        return Source.VOLTAGE if self.main_window.ds_voltage_2.isChecked() else Source.CURRENT

    def ds_get_smu_1(self):
        return self.get_smu_from_serial(self.main_window.smu_select_ds_1.currentText(), True)

    def ds_get_smu_2(self):
        return self.get_smu_from_serial(self.main_window.smu_select_ds_2.currentText(), True)

    def sm_get_smu_1(self):
        return self.get_smu_from_serial(self.main_window.smu_select_sm_1.currentText(), True)

    def sm_get_smu_2(self):
        return self.get_smu_from_serial(self.main_window.smu_select_sm_2.currentText(), True)

    def sm_get_sweep_smu(self):
        if self.main_window.sm_sweep_1.isChecked():
            return self.sm_get_smu_1()
        else:
            return self.sm_get_smu_2()

    def sm_get_constant_smu(self):
        if not self.main_window.sm_sweep_1.isChecked():
            return self.sm_get_smu_1()
        else:
            return self.sm_get_smu_2()

    @Slot()
    def ds_update_mode(self):
        self.main_window.ds_num_measurements.setDisabled(True)
        self.main_window.ds_num_measurements_label.setDisabled(True)
        self.main_window.ds_duration.setDisabled(True)
        self.main_window.ds_duration_label.setDisabled(True)

        if self.main_window.ds_fixed_duration.isChecked():
            self.main_window.ds_duration.setDisabled(False)
            self.main_window.ds_duration_label.setDisabled(False)
        elif self.main_window.ds_fixed_num.isChecked():
            self.main_window.ds_num_measurements.setDisabled(False)
            self.main_window.ds_num_measurements_label.setDisabled(False)

    @Slot()
    def ds_add_data(self, mp: MeasurementPoint):
        self.ds_last_run = pd.concat(
            (
                self.ds_last_run,
                pd.DataFrame(
                    {
                        "smu_1_voltage": [mp.smu_1_voltage],
                        "smu_1_current": [mp.smu_1_current],
                        "smu_2_voltage": [mp.smu_2_voltage],
                        "smu_2_current": [mp.smu_2_current],
                        "time": [mp.time],
                    }
                ),
            )
        )

        self.main_window.ds_plot_smu_1.update_data(self.ds_last_run)
        self.main_window.ds_plot_smu_2.update_data(self.ds_last_run)

    @Slot()
    def sm_add_data(self, mp: MeasurementPoint):
        self.sm_last_run[-1] = pd.concat(
            (
                self.sm_last_run[-1],
                pd.DataFrame(
                    {
                        "smu_1_voltage": [mp.smu_1_voltage],
                        "smu_1_current": [mp.smu_1_current],
                        "smu_2_voltage": [mp.smu_2_voltage],
                        "smu_2_current": [mp.smu_2_current],
                        "time": [mp.time],
                    }
                ),
            )
        )

        # TODO: Fix plotting stuff
        self.main_window.sm_plot_1.update_data(self.sm_last_run[-1])
        self.main_window.sm_plot_2.update_data(self.sm_last_run[-1])

    @Slot()
    def sm_run_measurement(self, quick_measurement=False):

        # Show a confirmation if we are about to overwrite data
        if len(self.sm_last_run[0]) > 0:

            confirmation_box = QMessageBox(
                QMessageBox.Icon.Warning,
                "Warning: Data will be discarded",
                "Continuing will discard data from previous run, are you sure you want to continue?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            )
            confirmation_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

            if confirmation_box.exec() == QMessageBox.StandardButton.Cancel:
                return

        self.sm_last_run = [initialize_data()]

        params = self.main_window.get_sweep_parameters(quick_measurement)

        self._thread_sweep = SweepMeasurementWorker(
            params,
            self.get_smu_from_serial(self.main_window.sm_sweep_smu.currentText()),
            self.get_smu_from_serial(self.main_window.sm_constant_smu.currentText()),
        )
        self._thread_sweep.finished.connect(self.sm_stop_measurement)
        self._thread_sweep.measurement_made.connect(self.sm_add_data)

        # Make sure that when a sweep finshes, we create a new column in data and start a new plot
        self._thread_sweep.sweep_complete.connect(lambda: self.sm_last_run.append(initialize_data()))

        # Disable/enable all necessary buttons
        c: QWidget
        for c in self.main_window.findChildren(QWidget, QRegularExpression("param|meta|smu|run|save")):
            c.setEnabled(False)

        self.main_window.sm_abort.setEnabled(True)

        # TODO: Fix plot stuff
        self._thread_sweep.sweep_complete.connect(self.main_window.sm_plot_1.start_new_curve)
        self._thread_sweep.sweep_complete.connect(self.main_window.sm_plot_2.start_new_curve)

        # Clear the plot from previous runs
        # TODO: Fix plot stuff
        self.main_window.sm_plot_1.reset()
        self.main_window.sm_plot_2.reset()

        self._thread_sweep.start()

        # Enable the stop measurement button and connect it to our thread
        self.main_window.sm_abort.clicked.connect(self._thread_sweep.stop)

    @Slot()
    def sm_stop_measurement(self):
        # Disable/enable all necessary buttons
        c: QWidget
        for c in self.main_window.findChildren(QWidget, QRegularExpression("param|meta|smu|run|save")):
            c.setEnabled(True)

        self.main_window.sm_abort.setEnabled(False)

    @Slot()
    def ds_stream_clicked(self):

        # Show a confirmation if we are about to overwrite data
        if len(self.ds_last_run) > 0:

            confirmation_box = QMessageBox(
                QMessageBox.Icon.Warning,
                "Warning: Data will be discarded",
                "Continuing will discard data from previous run, are you sure you want to continue?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            )
            confirmation_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

            if confirmation_box.exec() == QMessageBox.StandardButton.Cancel:
                return

        self.ds_last_run = initialize_data()

        params = self.main_window.get_stream_parameters()

        self._thread_datastream = DatastreamMeasurementWorker(params, self.ds_get_smu_1(), self.ds_get_smu_2())
        self._thread_datastream.finished.connect(self.ds_stop_streaming)
        self._thread_datastream.measurement_made.connect(self.ds_add_data)

        # Alter stream button connectins and text
        self.main_window.ds_stream.clicked.disconnect()
        self.main_window.ds_stream.clicked.connect(self._thread_datastream.stop)
        self.main_window.ds_stream.setText("Stop streaming")

        # Clear the plot from previous stream
        self.main_window.ds_plot_smu_1.reset()
        self.main_window.ds_plot_smu_2.reset()

        self._thread_datastream.start()

    @Slot()
    def ds_stop_streaming(self):
        self.main_window.ds_stream.clicked.disconnect()
        self.main_window.ds_stream.clicked.connect(self.ds_stream_clicked)
        self.main_window.ds_stream.setText("Start streaming")

        self.main_window.ds_save_data.setEnabled(True)

        # self.restore_all_enable_states()

    @Slot()
    def ds_choose_data_file_path(self):
        path, _ = QFileDialog(self.main_window).getSaveFileName(self.main_window, filter="*.xlsx")

        if path != "":
            self.ds_data_file_path = path
            self.main_window.ds_file_output_path.setText(self.ds_data_file_path)

    @Slot()
    def sm_choose_data_file_path(self):
        path, _ = QFileDialog(self.main_window).getSaveFileName(self.main_window, filter="*.xlsx")

        if path != "":
            self.sm_data_file_path = path
            self.main_window.sm_file_output_path.setText(self.sm_data_file_path)

    @Slot()
    def ds_save_last_run(self):

        # If we have not chosen a file path, choose one now
        if self.ds_data_file_path == "":
            self.ds_choose_data_file_path()

            # If we rejected choosing a file path, just return at this point
            if self.ds_data_file_path == "":
                return

        light_dark = ""

        if self.main_window.ds_light.isChecked():
            light_dark = "light"
        elif self.main_window.ds_dark.isChecked():
            light_dark = "dark"

        metadata = {
            "Wafer #": self.main_window.ds_wafer_num.text(),
            "Chip #": self.main_window.ds_chip_num.text(),
            "Step of Process": self.main_window.ds_step_of_process.text(),
            "Light/Dark": light_dark,
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Comments": self.main_window.ds_comments.toPlainText(),
        }

        # We need to reset the indexes
        self.ds_last_run = self.ds_last_run.reset_index(drop=True)

        write_data(self.ds_data_file_path, self.ds_last_run, metadata, include_time=True)

        # Reset last run data
        self.ds_last_run = initialize_data()
        self.main_window.ds_save_data.setEnabled(False)

    @Slot()
    def sm_save_last_run(self):

        # If we have not chosen a file path, choose one now
        if self.sm_data_file_path == "":
            self.sm_choose_data_file_path()

            # If we rejected choosing a file path, just return at this point
            if self.sm_data_file_path == "":
                return

        light_dark = ""

        if self.main_window.sm_light.isChecked():
            light_dark = "light"
        elif self.main_window.sm_dark.isChecked():
            light_dark = "dark"

        metadata = {
            "Wafer #": self.main_window.sm_wafer_num.text(),
            "Chip #": self.main_window.sm_chip_num.text(),
            "Step of Process": self.main_window.sm_step_of_process.text(),
            "Light/Dark": light_dark,
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Comments": self.main_window.sm_comments.toPlainText(),
        }

        for run in self.sm_last_run:
            run.reset_index(drop=True)
            write_data(self.sm_data_file_path, run, metadata, include_time=False)

        # Reset last run data
        self.sm_last_run = [initialize_data()]
        self.main_window.sm_save_data.setEnabled(False)


def set_input_mode(input: QDoubleSpinBox, is_step: bool, source: Source):

    if source is Source.VOLTAGE:
        input.setMaximum(21)
        input.setMinimum(-21)
        input.setSuffix(" V")
    else:
        input.setMaximum(1.05)
        input.setMinimum(-1.05)
        input.setSuffix(" A")

    if is_step:
        input.setMinimum(0.000001)


if __name__ == "__main__":

    import sys

    from PySide6.QtCore import QRegularExpression
    from PySide6.QtWidgets import QApplication

    # Create the application instance
    app = QApplication(sys.argv)

    controller = Controller()
    controller.smu_search_clicked()

    # print(controller.main_window.findChildren(QWidget, QRegularExpression("param|meta|smu|run|save")))

    # Enter the main event loop
    sys.exit(app.exec())
