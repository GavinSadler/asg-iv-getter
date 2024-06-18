from datetime import datetime
from typing import List

import pandas as pd
from PySide6.QtCore import QObject, Slot, Qt
from PySide6.QtWidgets import QComboBox, QDoubleSpinBox, QFileDialog, QMessageBox, QWidget, QListWidgetItem

from Data import Dataset, MeasurementPoint, write_data
from MainWindow import MainWindow
from Measurement import DatastreamMeasurementWorker, SweepMeasurementWorker
from SourceMeter import ConnectSMUWorker, Source, SourceMeter


class Controller(QObject):

    sourcemeters: List[SourceMeter]
    main_window: MainWindow

    ds_data_file_path: str
    sm_data_file_path: str

    sm_data: List[Dataset]
    ds_data: List[Dataset]

    sm_last_run: List[Dataset] | None
    ds_last_run: Dataset | None

    sm_last_measurement_quick_measurement: bool

    def __init__(self):
        super().__init__()

        # Initialize fields
        self.sourcemeters = []
        self.sm_data = []
        self.ds_data = []
        self.sm_last_run = None
        self.ds_last_run = None
        self.ds_data_file_path = ""
        self.sm_data_file_path = ""
        self.sm_last_measurement_quick_measurement = False

        # Create the user interface
        self.main_window = MainWindow()
        self.main_window.show()

        # === SMU Connection Tab ===
        self.main_window.smu_search.clicked.connect(self.smu_search_clicked)
        self.main_window.smu_connection_list.itemSelectionChanged.connect(self.smu_connection_selection_changed)
        self.main_window.smu_disconnect.clicked.connect(self.smu_disconnect_clicked)
        self.main_window.smu_identify.clicked.connect(self.smu_identify_clicked)

        # === Sweep tab ===
        self.main_window.sm_run_full_measurement.clicked.connect(self.sm_run_measurement)
        self.main_window.sm_run_quick_measurement.clicked.connect(lambda: self.sm_run_measurement(quick_measurement=True))

        self.main_window.sm_save_last_run.clicked.connect(self.sm_save_last_run)

        self.main_window.sm_file_output.clicked.connect(self.sm_choose_data_file_path)

        # === Datastream tab ===
        self.main_window.ds_stream.clicked.connect(self.ds_stream_clicked)

        self.main_window.ds_save_last_run.clicked.connect(self.ds_save_last_run)

        self.main_window.ds_file_output.clicked.connect(self.ds_choose_data_file_path)

        # === Data tab ===
        self.main_window.sweep_measurements.itemChanged.connect(self.update_data_plot)
        self.main_window.datastream_measurements.itemChanged.connect(self.update_data_plot)
        self.main_window.plot_parameters.clicked.connect(self.main_window.data_plot.show_plot_params_dialog)

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

    @Slot()
    def ds_add_data(self, mp: MeasurementPoint):
        self.ds_last_run.data = pd.concat(
            (
                self.ds_last_run.data,
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

        self.main_window.ds_plot_1.datasets = [self.ds_last_run]
        self.main_window.ds_plot_2.datasets = [self.ds_last_run]
        self.main_window.ds_plot_1.refresh()
        self.main_window.ds_plot_2.refresh()

    @Slot()
    def sm_add_data(self, mp: MeasurementPoint):
        self.sm_last_run[-1].data = pd.concat(
            (
                self.sm_last_run[-1].data,
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

        self.main_window.sm_plot_1.datasets = self.sm_last_run
        self.main_window.sm_plot_2.datasets = self.sm_last_run
        self.main_window.sm_plot_1.refresh()
        self.main_window.sm_plot_2.refresh()

    @Slot()
    def sm_run_measurement(self, quick_measurement=False):

        # Show a confirmation if we are about to overwrite data
        if self.sm_last_run is not None and not self.sm_last_measurement_quick_measurement:

            confirmation_box = QMessageBox(
                QMessageBox.Icon.Warning,
                "Warning: Data will be discarded",
                "Continuing will discard data from previous run, are you sure you want to continue?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            )
            confirmation_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

            if confirmation_box.exec() == QMessageBox.StandardButton.Cancel:
                return

        # Used to make sure that we don't bother the user if they're overwriting a quick measurement
        self.sm_last_measurement_quick_measurement = quick_measurement

        # Reset the last run field
        self.sm_last_run = [Dataset.initialize(self.main_window.get_sm_metadata())]

        # Create the sweeping thread
        self._thread_sweep = SweepMeasurementWorker(
            self.main_window.get_sweep_parameters(quick_measurement),
            self.get_smu_from_serial(self.main_window.sm_sweep_smu.currentText()),
            self.get_smu_from_serial(self.main_window.sm_constant_smu.currentText()),
        )
        self._thread_sweep.finished.connect(self.sm_stop_measurement)
        self._thread_sweep.measurement_made.connect(self.sm_add_data)

        # Make sure that when a sweep finshes, we create a new column in data and start new plot curves
        self._thread_sweep.sweep_complete.connect(lambda: self.sm_last_run.append(Dataset.initialize(self.main_window.get_sm_metadata())))

        # Disable/enable all necessary buttons
        c: QWidget
        for c in self.main_window.findChildren(QWidget, QRegularExpression("param|meta|smu|sm_run|sm_save|ds_stream")):
            c.setEnabled(False)

        # Enable the stop measurement button and connect it to our thread
        self.main_window.sm_abort.setEnabled(True)
        self.main_window.sm_abort.clicked.connect(self._thread_sweep.stop)

        # Clear the plot from previous runs
        self.main_window.sm_plot_1.reset()
        self.main_window.sm_plot_2.reset()

        # Start the sweep
        self._thread_sweep.start()

    @Slot()
    def sm_stop_measurement(self):
        # Disable/enable all necessary buttons
        c: QWidget
        for c in self.main_window.findChildren(QWidget, QRegularExpression("param|meta|smu|sm_run|sm_save|ds_stream")):
            c.setEnabled(True)
        
        # Crappy fix for disabling certain buttons in datastream tab
        self.main_window.ds_params_changed()

        self.main_window.sm_abort.setEnabled(False)

    @Slot()
    def ds_stream_clicked(self):

        # Show a confirmation if we are about to overwrite data
        if self.ds_last_run is not None:

            confirmation_box = QMessageBox(
                QMessageBox.Icon.Warning,
                "Warning: Data will be discarded",
                "Continuing will discard data from previous run, are you sure you want to continue?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            )
            confirmation_box.setDefaultButton(QMessageBox.StandardButton.Cancel)

            if confirmation_box.exec() == QMessageBox.StandardButton.Cancel:
                return

        self.ds_last_run = Dataset.initialize(self.main_window.get_ds_metadata())

        self._thread_datastream = DatastreamMeasurementWorker(
            self.main_window.get_stream_parameters(),
            self.get_smu_from_serial(self.main_window.ds_smu_1.currentText()),
            self.get_smu_from_serial(self.main_window.ds_smu_2.currentText()),
        )

        self._thread_datastream.finished.connect(self.ds_stop_streaming)
        self._thread_datastream.measurement_made.connect(self.ds_add_data)

        # Disable/enable all necessary buttons
        c: QWidget
        for c in self.main_window.findChildren(QWidget, QRegularExpression("param|meta|smu|sm_run|ds_save")):
            c.setEnabled(False)

        # Alter stream button connectins and text
        self.main_window.ds_stream.clicked.disconnect()
        self.main_window.ds_stream.clicked.connect(self._thread_datastream.stop)
        self.main_window.ds_stream.setText("Stop streaming")

        # Clear the plot from previous stream
        self.main_window.ds_plot_1.reset()
        self.main_window.ds_plot_2.reset()

        self._thread_datastream.start()

    @Slot()
    def ds_stop_streaming(self):
        # Disable/enable all necessary buttons
        c: QWidget
        for c in self.main_window.findChildren(QWidget, QRegularExpression("param|meta|smu|sm_run|ds_save")):
            c.setEnabled(True)
        
        # Crappy fix for disabling certain buttons in datastream tab
        self.main_window.ds_params_changed()

        self.main_window.ds_stream.clicked.disconnect()
        self.main_window.ds_stream.clicked.connect(self.ds_stream_clicked)
        self.main_window.ds_stream.setText("Start streaming")

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

        # We need to reset the indexes
        self.ds_last_run.data = self.ds_last_run.data.reset_index(drop=True)

        # Switch out the metadata with new metadata, just in case the user changes it before saving
        self.ds_last_run.metadata = self.main_window.get_ds_metadata()

        try:
            write_data(self.ds_data_file_path, self.ds_last_run)
        except PermissionError:
            QMessageBox(
                QMessageBox.Icon.Critical,
                "Error: Could not save data",
                f"An error occured when trying to save the last run's data to {self.sm_data_file_path}.\nIt is possible that the file open in another program.",
                QMessageBox.StandardButton.Ok,
                parent=self.main_window,
            ).show()
            return

        # Store the data here
        self.ds_data.append(self.ds_last_run)
        self.update_data_tab()

        # Reset last run data
        self.ds_last_run = None
        self.main_window.ds_save_last_run.setEnabled(False)

    @Slot()
    def sm_save_last_run(self):

        # If we have not chosen a file path, choose one now
        if self.sm_data_file_path == "":
            self.sm_choose_data_file_path()

            # If we rejected choosing a file path, just return at this point
            if self.sm_data_file_path == "":
                return
        # TODO: Handle data saving in a more stable way
        try:
            for run in self.sm_last_run:
                run.data.reset_index(drop=True)
                # Switch out the metadata with new metadata, just in case the user changes it before saving
                run.metadata = self.main_window.get_sm_metadata()
                # Save the data from this run in the data variable
                self.sm_data.append(run)
                write_data(self.sm_data_file_path, run)
        except PermissionError:
            QMessageBox(
                QMessageBox.Icon.Critical,
                "Error: Could not save data",
                f"An error occured when trying to save the last run's data to {self.sm_data_file_path}.\nIt is possible that the file open in another program.",
                QMessageBox.StandardButton.Ok,
                parent=self.main_window,
            ).show()
            return

        self.update_data_tab()

        # Reset last run data
        self.sm_last_run = None
        self.main_window.sm_save_last_run.setEnabled(False)

    def update_data_plot(self, item: QListWidgetItem):

        if item.checkState() == Qt.CheckState.Checked:
            self.main_window.data_plot.datasets.append(item.data_reference)
            self.main_window.data_plot.refresh()
        elif item.checkState() == Qt.CheckState.Unchecked:
            self.main_window.data_plot.datasets.remove(item.data_reference)
            self.main_window.data_plot.refresh()

    def update_data_tab(self):
        self.main_window.sweep_measurements.clear()
        self.main_window.datastream_measurements.clear()

        self.main_window.data_plot.datasets = []
        self.main_window.data_plot.refresh()

        for d in self.sm_data:
            li = QListWidgetItem(f"{d.metadata.wafer_number} {d.metadata.chip_number} {d.metadata.step_of_process}")
            li.setCheckState(Qt.CheckState.Unchecked)
            li.data_reference = d
            self.main_window.sweep_measurements.addItem(li)

        for d in self.ds_data:
            li = QListWidgetItem(f"{d.metadata.wafer_number} {d.metadata.chip_number} {d.metadata.step_of_process}")
            li.setCheckState(Qt.CheckState.Unchecked)
            li.data_reference = d
            self.main_window.datastream_measurements.addItem(li)


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
