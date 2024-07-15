import os
from typing import List

import pandas as pd
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from Data import Dataset, MeasurementPoint
from MainWindow import MainWindow
from Measurement import DatastreamMeasurementWorker, SweepMeasurementWorker
from SMUSeachDialog import SMUSearchDialog
from SourceMeter import ConnectSMUWorker, Source, SourceMeter


class Controller(QtCore.QObject):

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
        self.sm_last_run = []
        self.ds_last_run = None
        self.ds_data_file_path = ""
        self.sm_data_file_path = ""
        self.sm_last_measurement_quick_measurement = False

        # Create the user interface
        self.main_window = MainWindow()
        self.main_window.show()

        self.main_window.menubar_sourcemeter_connections.triggered.connect(lambda _: self.update_smu_uis(SMUSearchDialog(self.sourcemeters).get_sourcemeters()))

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

    @QtCore.Slot()
    def update_smu_uis(self, new_connections: List[SourceMeter]):

        self.sourcemeters = new_connections

        combo_box: QtWidgets.QComboBox

        for combo_box in self.main_window.findChildren(QtWidgets.QComboBox):

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

    @QtCore.Slot()
    def ds_add_data(self, mp: MeasurementPoint):
        self.ds_last_run.smu_1_current.append(mp.smu_1_current)
        self.ds_last_run.smu_1_voltage.append(mp.smu_1_voltage)
        self.ds_last_run.smu_2_current.append(mp.smu_2_current)
        self.ds_last_run.smu_2_voltage.append(mp.smu_2_voltage)
        self.ds_last_run.time.append(mp.time)

        self.main_window.ds_plot_1.refresh_latest()
        self.main_window.ds_plot_2.refresh_latest()

    @QtCore.Slot()
    def sm_add_data(self, mp: MeasurementPoint):
        self.sm_last_run[-1].smu_1_current.append(mp.smu_1_current)
        self.sm_last_run[-1].smu_1_voltage.append(mp.smu_1_voltage)
        self.sm_last_run[-1].smu_2_current.append(mp.smu_2_current)
        self.sm_last_run[-1].smu_2_voltage.append(mp.smu_2_voltage)
        self.sm_last_run[-1].time.append(mp.time)

        self.main_window.sm_plot_1.refresh_latest()
        self.main_window.sm_plot_2.refresh_latest()

    def initialize_sm_dataset(self, constant_supply_value: float):
        d = Dataset()
        d.metadata = self.main_window.get_sm_metadata()
        d.write_time = self.main_window.sm_meta_time_data.isChecked()
        d.metadata["Constant Supply"] = constant_supply_value

        return d

    def initialize_ds_dataset(self):
        d = Dataset()
        d.metadata = self.main_window.get_ds_metadata()
        d.write_time = self.main_window.ds_meta_time_data.isChecked()
        d.metadata["Constant Supply"] = ""

        return d

    @QtCore.Slot()
    def sm_run_measurement(self, quick_measurement=False):

        # Show a confirmation if we are about to overwrite data
        if len(self.sm_last_run) > 0 and not self.sm_last_measurement_quick_measurement:

            confirmation_box = QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Warning,
                "Warning: Data will be discarded",
                "Continuing will discard data from previous run, are you sure you want to continue?",
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.Cancel,
            )
            confirmation_box.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Cancel)

            if confirmation_box.exec() == QtWidgets.QMessageBox.StandardButton.Cancel:
                return

        # Used to make sure that we don't bother the user if they're overwriting a quick measurement
        self.sm_last_measurement_quick_measurement = quick_measurement

        sweep_params = self.main_window.get_sweep_parameters(quick_measurement)

        # Create the sweeping thread
        self._thread_sweep = SweepMeasurementWorker(
            sweep_params,
            self.get_smu_from_serial(self.main_window.sm_sweep_smu_select.currentText()),
            self.get_smu_from_serial(self.main_window.sm_constant_smu_select.currentText()),
        )

        # Reset the last run field
        self.sm_last_run = [self.initialize_sm_dataset(sweep_params.constant_start)]

        self._thread_sweep.measurement_made.connect(self.sm_add_data)

        # Make sure that when a sweep finshes, we create a new column in data
        # and start new plot curves. We need to calculate what the constant
        # current for this new dataset will be, as well. This is simply what the
        # current constant current is + whatever step we have set
        self._thread_sweep.sweep_complete.connect(
            lambda _: self.sm_last_run.append(self.initialize_sm_dataset(self._thread_sweep.constant_supply_now + sweep_params.constant_step))
        )
        
        # ... and add those newly initialized datasets to the plot
        self._thread_sweep.sweep_complete.connect(lambda _: self.main_window.sm_plot_1.add_dataset(self.sm_last_run[-1]))
        self._thread_sweep.sweep_complete.connect(lambda _: self.main_window.sm_plot_2.add_dataset(self.sm_last_run[-1]))

        # Super hacky, but when a test finishes, we need to remove the last dataset and re-add it
        self._thread_sweep.test_complete.connect(lambda: self.sm_last_run.pop())
        self._thread_sweep.test_complete.connect(lambda: self.main_window.sm_plot_1.remove_last_dataset())
        self._thread_sweep.test_complete.connect(lambda: self.main_window.sm_plot_2.remove_last_dataset())
        self._thread_sweep.test_complete.connect(lambda: self.sm_last_run.append(self.initialize_sm_dataset(sweep_params.constant_start)))
        self._thread_sweep.test_complete.connect(lambda: self.main_window.sm_plot_1.add_dataset(self.sm_last_run[-1]))
        self._thread_sweep.test_complete.connect(lambda: self.main_window.sm_plot_2.add_dataset(self.sm_last_run[-1]))

        # A bit of a hack, but the line above will create an extra dataset. These line will remove it
        self._thread_sweep.finished.connect(lambda: self.sm_last_run.pop())
        self._thread_sweep.finished.connect(lambda: self.main_window.sm_plot_1.remove_last_dataset())
        self._thread_sweep.finished.connect(lambda: self.main_window.sm_plot_2.remove_last_dataset())
        
        
        self._thread_sweep.finished.connect(self.sm_stop_measurement)

        # Disable/enable all necessary buttons
        c: QtWidgets.QWidget
        for c in self.main_window.findChildren(QtWidgets.QWidget, QtCore.QRegularExpression("param|meta|smu|sm_run|sm_save|ds_stream|tab_data")):
            c.setEnabled(False)

        # Enable the stop measurement button and connect it to our thread
        self.main_window.sm_abort.setEnabled(True)
        self.main_window.sm_abort.clicked.connect(self._thread_sweep.stop)

        # Clear the plot from previous runs
        self.main_window.sm_plot_1.reset()
        self.main_window.sm_plot_2.reset()
        
        # Add the new datasets to the plots
        self.main_window.sm_plot_1.add_dataset(self.sm_last_run[-1])
        self.main_window.sm_plot_2.add_dataset(self.sm_last_run[-1])

        # Start the sweep
        self._thread_sweep.start()

    @QtCore.Slot()
    def sm_stop_measurement(self):
        # Disable/enable all necessary buttons
        c: QtWidgets.QWidget
        for c in self.main_window.findChildren(QtWidgets.QWidget, QtCore.QRegularExpression("param|meta|smu|sm_run|sm_save|ds_stream|tab_data")):
            c.setEnabled(True)

        # Crappy fix for disabling certain buttons in datastream tab
        self.main_window.ds_params_changed()

        self.update_data_tab()

        self.main_window.sm_abort.setEnabled(False)

    @QtCore.Slot()
    def ds_stream_clicked(self):

        # Show a confirmation if we are about to overwrite data
        if self.ds_last_run is not None:

            confirmation_box = QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Warning,
                "Warning: Data will be discarded",
                "Continuing will discard data from previous run, are you sure you want to continue?",
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.Cancel,
            )
            confirmation_box.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Cancel)

            if confirmation_box.exec() == QtWidgets.QMessageBox.StandardButton.Cancel:
                return

        # Reset last run dataset
        self.ds_last_run = self.initialize_ds_dataset()
        
        # Clear the plot from previous stream
        self.main_window.ds_plot_1.reset()
        self.main_window.ds_plot_2.reset()
        
        self.main_window.ds_plot_1.add_dataset(self.ds_last_run)
        self.main_window.ds_plot_2.add_dataset(self.ds_last_run)
        
        self._thread_datastream = DatastreamMeasurementWorker(
            self.main_window.get_stream_parameters(),
            self.get_smu_from_serial(self.main_window.ds_smu_select_1.currentText()),
            self.get_smu_from_serial(self.main_window.ds_smu_select_2.currentText()),
        )

        self._thread_datastream.finished.connect(self.ds_stop_streaming)
        self._thread_datastream.measurement_made.connect(self.ds_add_data)

        # Disable/enable all necessary buttons
        c: QtWidgets.QWidget
        for c in self.main_window.findChildren(QtWidgets.QWidget, QtCore.QRegularExpression("param|meta|smu|sm_run|ds_save|tab_data_view|tab_sweep_measurement")):
            c.setEnabled(False)

        # Alter stream button connectins and text
        self.main_window.ds_stream.clicked.disconnect()
        self.main_window.ds_stream.clicked.connect(self._thread_datastream.stop)
        self.main_window.ds_stream.setText("Stop streaming")

        self._thread_datastream.start()

    @QtCore.Slot()
    def ds_stop_streaming(self):
        # Disable/enable all necessary buttons
        c: QtWidgets.QWidget
        for c in self.main_window.findChildren(QtWidgets.QWidget, QtCore.QRegularExpression("param|meta|smu|sm_run|ds_save|tab_data_view|tab_sweep_measurement")):
            c.setEnabled(True)

        # Crappy fix for disabling certain buttons in datastream tab
        self.main_window.ds_params_changed()

        self.update_data_tab()

        self.main_window.ds_stream.clicked.disconnect()
        self.main_window.ds_stream.clicked.connect(self.ds_stream_clicked)
        self.main_window.ds_stream.setText("Start streaming")

    @QtCore.Slot()
    def ds_choose_data_file_path(self):
        path, _ = QtWidgets.QFileDialog(self.main_window).getSaveFileName(self.main_window, filter="*.xlsx")

        if path != "":
            self.ds_data_file_path = path
            self.main_window.ds_file_output_path.setText(self.ds_data_file_path)

    @QtCore.Slot()
    def sm_choose_data_file_path(self):
        path, _ = QtWidgets.QFileDialog(self.main_window).getSaveFileName(self.main_window, filter="*.xlsx")

        if path != "":
            self.sm_data_file_path = path
            self.main_window.sm_file_output_path.setText(self.sm_data_file_path)

    @QtCore.Slot()
    def ds_save_last_run(self):

        # If we have not chosen a file path, choose one now
        if self.ds_data_file_path == "":
            self.ds_choose_data_file_path()

            # If we rejected choosing a file path, just return at this point
            if self.ds_data_file_path == "":
                return

        # Update the metadata - its possible that the user updated the data
        self.ds_last_run.metadata.update(self.main_window.get_ds_metadata())
        self.ds_last_run.write_time = self.main_window.ds_meta_time_data.isChecked()

        try:
            # Write if no file exists, otherwise append to the existing file
            write_mode = "w" if not os.path.exists(self.ds_data_file_path) else "a"
            
            with pd.ExcelWriter(self.ds_data_file_path, mode=write_mode, if_sheet_exists=("overlay" if write_mode == "a" else None), engine="openpyxl") as writer:
                self.ds_last_run.write_to_excel(writer)
            
        except PermissionError:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Error: Could not save data",
                f"An error occured when trying to save the last run's data to {self.sm_data_file_path}.\nIt is possible that the file open in another program.",
                QtWidgets.QMessageBox.StandardButton.Ok,
                parent=self.main_window,
            ).show()
            return

        # Store the data here
        self.ds_data.append(self.ds_last_run)

        # Reset last run data
        self.ds_last_run = None
        self.main_window.ds_save_last_run.setEnabled(False)

        self.update_data_tab()

    @QtCore.Slot()
    def sm_save_last_run(self):

        # If we have not chosen a file path, choose one now
        if self.sm_data_file_path == "":
            self.sm_choose_data_file_path()

            # If we rejected choosing a file path, just return at this point
            if self.sm_data_file_path == "":
                return
            
        # TODO: Handle data saving in a more stable way
        try:
            # Write if no file exists, otherwise append to the existing file
            write_mode = "w" if not os.path.exists(self.sm_data_file_path) else "a"
            
            with pd.ExcelWriter(self.sm_data_file_path, mode=write_mode, if_sheet_exists=("overlay" if write_mode == "a" else None), engine="openpyxl") as writer:
                for run in self.sm_last_run:
                    
                    # Update the metadata - its possible that the user updated the data
                    run.metadata.update(self.main_window.get_sm_metadata())
                    run.write_time = self.main_window.sm_meta_time_data.isChecked()
                    
                    run.write_to_excel(writer)

                    # Save the data from this run in the data variable
                    self.sm_data.append(run)
        except PermissionError:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Error: Could not save data",
                f"An error occured when trying to save the last run's data to {self.sm_data_file_path}.\nIt is possible that the file open in another program.",
                QtWidgets.QMessageBox.StandardButton.Ok,
                parent=self.main_window,
            ).show()
            return

        # Reset last run data
        self.sm_last_run = []
        self.main_window.sm_save_last_run.setEnabled(False)

        self.update_data_tab()

    def update_data_plot(self, item: QtWidgets.QListWidgetItem):

        if item.checkState() == QtCore.Qt.CheckState.Checked:
            self.main_window.data_plot.datasets.append(item.data_reference)
            self.main_window.data_plot.refresh_all()
        elif item.checkState() == QtCore.Qt.CheckState.Unchecked:
            self.main_window.data_plot.datasets.remove(item.data_reference)
            self.main_window.data_plot.refresh_all()

    def update_data_tab(self):
        self.main_window.sweep_measurements.clear()
        self.main_window.datastream_measurements.clear()

        self.main_window.data_plot.datasets.clear()
        self.main_window.data_plot.refresh_all()

        # Add the last run that might not be saved yet
        for run in self.sm_last_run:
            # Make a copy of these runs because we want to add (Last run) before the wafer number
            r = run.copy()
            r.metadata["Wafer #"] = f"(Last run) {r.metadata["Wafer #"]}"

            li = QtWidgets.QListWidgetItem(f"{str(r.metadata.get("Wafer #")) or ''} {str(r.metadata.get("Comments")) or ''} {str(r.metadata.get("Constant Supply")) or ''}")
            li.setCheckState(QtCore.Qt.CheckState.Unchecked)
            li.data_reference = r

            self.main_window.sweep_measurements.addItem(li)

        # This is for the datastream's last run
        if self.ds_last_run is not None:
            r = self.ds_last_run.copy()
            r.metadata["Wafer #"] = f"(Last run) {r.metadata["Wafer #"]}"

            li = QtWidgets.QListWidgetItem(f"{str(r.metadata.get("Wafer #")) or ''} {str(r.metadata.get("Comments")) or ''}")
            li.setCheckState(QtCore.Qt.CheckState.Unchecked)
            li.data_reference = r

            self.main_window.datastream_measurements.addItem(li)

        # Now go through the already saved datasets and add those
        for d in self.sm_data:
            li = QtWidgets.QListWidgetItem(f"{str(d.metadata.get("Wafer #")) or ''} {str(d.metadata.get("Comments")) or ''} {str(d.metadata.get("Constant Supply")) or ''}")
            li.setCheckState(QtCore.Qt.CheckState.Unchecked)
            li.data_reference = d

            self.main_window.sweep_measurements.addItem(li)

        for d in self.ds_data:
            li = QtWidgets.QListWidgetItem(f"{str(d.metadata.get("Wafer #")) or ''} {str(d.metadata.get("Comments")) or ''}")
            li.setCheckState(QtCore.Qt.CheckState.Unchecked)
            li.data_reference = d

            self.main_window.datastream_measurements.addItem(li)


def set_input_mode(input: QtWidgets.QDoubleSpinBox, is_step: bool, source: Source):

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

    from PySide6.QtWidgets import QApplication

    # Create the application instance
    app = QApplication(sys.argv)

    controller = Controller()

    # This will attempt to connect to the SMUs on launch
    smu_connection_worker = ConnectSMUWorker(controller)
    smu_connection_worker.connections_made.connect(controller.update_smu_uis)
    smu_connection_worker.start()

    # Enter the main event loop
    sys.exit(app.exec())
