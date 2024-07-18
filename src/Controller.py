import json
import os
from typing import Dict, List

import pandas as pd
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from Data import Dataset, MeasurementPoint
from MainWindow import MainWindow
from Measurement import DatastreamMeasurementWorker, SweepMeasurementWorker
from PlotParamsDialog import PlotParam
from SMUSeachDialog import SMUSearchDialog
from SourceMeter import ConnectSMUWorker, SourceMeter


class Controller(QtCore.QObject):
    sourcemeters: List[SourceMeter]
    sourcemeter_names: Dict[str, str]

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
        self.sourcemeter_names = {}
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

        self.main_window.menubar_sourcemeter_connections.triggered.connect(
            lambda _: self.update_smu_uis(SMUSearchDialog(self.sourcemeters, self.sourcemeter_names, self.main_window).get_sourcemeters())
        )

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

        # === Menubar connections ===
        self.main_window.menubar_save_configuration.triggered.connect(self.save_configuration)
        self.main_window.menubar_load_configuration.triggered.connect(self.load_configuration)

        # === SMU combo box change connections ===
        self.main_window.sm_sweep_smu_select.currentTextChanged.connect(self.update_plot_labels)
        self.main_window.sm_constant_smu_select.currentTextChanged.connect(self.update_plot_labels)
        self.main_window.ds_smu_select_1.currentTextChanged.connect(self.update_plot_labels)
        self.main_window.ds_smu_select_2.currentTextChanged.connect(self.update_plot_labels)
        self.main_window.data_smu_select_1.currentTextChanged.connect(self.update_plot_labels)
        self.main_window.data_smu_select_2.currentTextChanged.connect(self.update_plot_labels)

        # Load in default configuration
        if os.path.exists("config_default.json"):
            self.load_configuration_from_file("config_default.json")

    @QtCore.Slot()
    def update_smu_uis(self, new_connections: List[SourceMeter]):

        self.sourcemeters = new_connections

        # Apply names to the sourcemeters
        for smu in self.sourcemeters:
            if smu.name is None:
                smu.name = self.sourcemeter_names.get(smu.serial_number)

        combo_box: QtWidgets.QComboBox

        for combo_box in self.main_window.findChildren(QtWidgets.QComboBox):

            if "smu_select" in combo_box.objectName():
                combo_box.clear()
                combo_box.addItem("Simulated")

                for smu in self.sourcemeters:
                    combo_box.addItem(smu.get_label())

        # Plot labels depend on the SMU UI and their labels
        self.update_plot_labels()

    def get_smu_from_label(self, label: str, allow_simulated=True):
        for smu in self.sourcemeters:
            if "(" in label:
                label = label.split("(")[1][:-1]

            if smu.serial_number == label:
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
        d.metadata["Constant Supply"] = f"{constant_supply_value:.3f}"

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
            self.get_smu_from_label(self.main_window.sm_sweep_smu_select.currentText()),
            self.get_smu_from_label(self.main_window.sm_constant_smu_select.currentText()),
        )

        # Reset the last run field
        self.sm_last_run = []

        # Make all connections to the worker thread
        self._thread_sweep.measurement_made.connect(self.sm_add_data)
        self._thread_sweep.sweep_begin.connect(lambda constant_supply_output: self.sm_last_run.append(self.initialize_sm_dataset(constant_supply_output)))
        self._thread_sweep.sweep_begin.connect(lambda _: self.main_window.sm_plot_1.add_dataset(self.sm_last_run[-1]))
        self._thread_sweep.sweep_begin.connect(lambda _: self.main_window.sm_plot_2.add_dataset(self.sm_last_run[-1]))

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
            self.get_smu_from_label(self.main_window.ds_smu_select_1.currentText()),
            self.get_smu_from_label(self.main_window.ds_smu_select_2.currentText()),
        )

        self._thread_datastream.finished.connect(self.ds_stop_streaming)
        self._thread_datastream.measurement_made.connect(self.ds_add_data)

        # Disable/enable all necessary buttons
        c: QtWidgets.QWidget
        for c in self.main_window.findChildren(
            QtWidgets.QWidget, QtCore.QRegularExpression("param|meta|smu|sm_run|ds_save|tab_data_view|tab_sweep_measurement")
        ):
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
        for c in self.main_window.findChildren(
            QtWidgets.QWidget, QtCore.QRegularExpression("param|meta|smu|sm_run|ds_save|tab_data_view|tab_sweep_measurement")
        ):
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

            with pd.ExcelWriter(
                self.ds_data_file_path, mode=write_mode, if_sheet_exists=("overlay" if write_mode == "a" else None), engine="openpyxl"
            ) as writer:
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

            with pd.ExcelWriter(self.sm_data_file_path, mode=write_mode, if_sheet_exists=("overlay" if write_mode == "a" else None)) as writer:
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
                f"An error occurred when trying to save the last run's data to {self.sm_data_file_path}.\nIt is possible that the file open in another program.",
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

            li = QtWidgets.QListWidgetItem(r.get_label())
            li.setCheckState(QtCore.Qt.CheckState.Unchecked)
            li.data_reference = r

            self.main_window.sweep_measurements.addItem(li)

        # This is for the datastream's last run
        if self.ds_last_run is not None:
            r = self.ds_last_run.copy()
            r.metadata["Wafer #"] = f"(Last run) {r.metadata["Wafer #"]}"

            li = QtWidgets.QListWidgetItem(r.get_label())
            li.setCheckState(QtCore.Qt.CheckState.Unchecked)
            li.data_reference = r

            self.main_window.datastream_measurements.addItem(li)

        # Now go through the already saved datasets and add those
        for d in self.sm_data:
            li = QtWidgets.QListWidgetItem(d.get_label())
            li.setCheckState(QtCore.Qt.CheckState.Unchecked)
            li.data_reference = d

            self.main_window.sweep_measurements.addItem(li)

        for d in self.ds_data:
            li = QtWidgets.QListWidgetItem(d.get_label())
            li.setCheckState(QtCore.Qt.CheckState.Unchecked)
            li.data_reference = d

            self.main_window.datastream_measurements.addItem(li)

    @QtCore.Slot()
    def save_configuration(self):
        params = self.main_window.findChildren(QtWidgets.QWidget, QtCore.QRegularExpression("param"))

        config = {"parameter_values": {}, "sourcemeter_names": {}}

        # Params from ui elements
        for p in params:
            if isinstance(p, (QtWidgets.QSpinBox, QtWidgets.QDoubleSpinBox)):
                config["parameter_values"][p.objectName()] = p.value()
            elif isinstance(p, (QtWidgets.QRadioButton, QtWidgets.QCheckBox)):
                config["parameter_values"][p.objectName()] = p.isChecked()

        # Plot params
        config["parameter_values"]["sm_plot_1.x_param"] = self.main_window.sm_plot_1.x_param.name
        config["parameter_values"]["sm_plot_1.y_param"] = self.main_window.sm_plot_1.y_param.name
        config["parameter_values"]["sm_plot_2.x_param"] = self.main_window.sm_plot_2.x_param.name
        config["parameter_values"]["sm_plot_2.y_param"] = self.main_window.sm_plot_2.y_param.name
        config["parameter_values"]["ds_plot_1.x_param"] = self.main_window.ds_plot_1.x_param.name
        config["parameter_values"]["ds_plot_1.y_param"] = self.main_window.ds_plot_1.y_param.name
        config["parameter_values"]["ds_plot_2.x_param"] = self.main_window.ds_plot_2.x_param.name
        config["parameter_values"]["ds_plot_2.y_param"] = self.main_window.ds_plot_2.y_param.name
        config["parameter_values"]["data_plot.x_param"] = self.main_window.data_plot.x_param.name
        config["parameter_values"]["data_plot.y_param"] = self.main_window.data_plot.y_param.name

        # SMU names
        for smu in self.sourcemeters:
            if smu.name and not smu.simulated:
                config["sourcemeter_names"][smu.serial_number] = smu.name

        # See where the user wants to save the file
        path, _ = QtWidgets.QFileDialog(self.main_window).getSaveFileName(self.main_window, filter="*.json", dir="config_default.json")

        if path == "":
            return

        # Write the config to disk
        with open(path, "w") as fp:
            json.dump(config, fp, indent=4)

    @QtCore.Slot()
    def load_configuration(self):
        # See what file the user wants to load
        path, _ = QtWidgets.QFileDialog(self.main_window).getOpenFileName(self.main_window, filter="*.json")

        if path == "":
            return

        self.load_configuration_from_file(path)

    def load_configuration_from_file(self, file_path: str):

        # Read in the values from the file
        try:
            with open(file_path, "r") as fp:
                config: Dict[str, str | int | float | bool] = json.load(fp)
        except json.JSONDecodeError:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Warning,
                "Warning: Error loading configuration",
                "It seems like the loaded configuration file is malformed. Default settings will be applied instead.",
                QtWidgets.QMessageBox.StandardButton.Ok,
                parent=self.main_window,
            ).show()
            return

        if config.get("parameter_values") is None:
            return

        # Apply those values
        for object_name, value in config["parameter_values"].items():
            c: QtWidgets.QWidget = self.main_window.findChild(QtWidgets.QWidget, object_name)

            # In the event that a non-ui element config option is encountered
            if c is None:
                continue

            # Different objects have to be treated differently
            if isinstance(c, (QtWidgets.QSpinBox, QtWidgets.QDoubleSpinBox)):
                c.setValue(value)
            elif isinstance(c, (QtWidgets.QRadioButton, QtWidgets.QCheckBox)):
                c.setChecked(value)

        # Set plot params appropriately. Wrap in a keyerror in the event that these settings don't exist
        try:
            self.main_window.sm_plot_1.set_plot_parameters(
                PlotParam(config["parameter_values"]["sm_plot_1.x_param"]), PlotParam(config["parameter_values"]["sm_plot_1.y_param"])
            )
            self.main_window.sm_plot_2.set_plot_parameters(
                PlotParam(config["parameter_values"]["sm_plot_2.x_param"]), PlotParam(config["parameter_values"]["sm_plot_2.y_param"])
            )
            self.main_window.ds_plot_1.set_plot_parameters(
                PlotParam(config["parameter_values"]["ds_plot_1.x_param"]), PlotParam(config["parameter_values"]["ds_plot_1.y_param"])
            )
            self.main_window.ds_plot_2.set_plot_parameters(
                PlotParam(config["parameter_values"]["ds_plot_2.x_param"]), PlotParam(config["parameter_values"]["ds_plot_2.y_param"])
            )
            self.main_window.data_plot.set_plot_parameters(
                PlotParam(config["parameter_values"]["data_plot.x_param"]), PlotParam(config["parameter_values"]["data_plot.y_param"])
            )
        except KeyError:
            pass

        # Load in sourcemeter names
        self.sourcemeter_names = config.get("sourcemeter_names") or {}

    def update_plot_labels(self):

        sweep = self.get_smu_from_label(self.main_window.sm_sweep_smu_select.currentText()).get_label(include_serial=False)
        constant = self.get_smu_from_label(self.main_window.sm_constant_smu_select.currentText()).get_label(include_serial=False)
        ds1 = self.get_smu_from_label(self.main_window.ds_smu_select_1.currentText()).get_label(include_serial=False)
        ds2 = self.get_smu_from_label(self.main_window.ds_smu_select_2.currentText()).get_label(include_serial=False)
        data_1 = self.get_smu_from_label(self.main_window.data_smu_select_1.currentText()).get_label(include_serial=False)
        data_2 = self.get_smu_from_label(self.main_window.data_smu_select_2.currentText()).get_label(include_serial=False)

        self.main_window.sm_plot_1.set_labels(sweep, constant)
        self.main_window.sm_plot_2.set_labels(sweep, constant)
        self.main_window.ds_plot_1.set_labels(ds1, ds2)
        self.main_window.ds_plot_2.set_labels(ds1, ds2)
        self.main_window.data_plot.set_labels(data_1, data_2)
        self.main_window.data_plot.set_labels(data_1, data_2)


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
