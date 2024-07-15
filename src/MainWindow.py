import json
import os
from datetime import datetime
from typing import Dict

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from Measurement import DatastreamMode, DatastreamParameters, SweepParameters
from PlotParamsDialog import PlotParam
from SourceMeter import Source
from UserInterface.ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)

        # Load in defaults
        if os.path.exists("config_default.json"):
            self.load_configuration_from_file("config_default.json")

        # === Data stream configuration change connections ===
        self.ds_param_continuous.clicked.connect(self.ds_params_changed)
        self.ds_param_fixed_duration.clicked.connect(self.ds_params_changed)
        self.ds_param_fixed_number.clicked.connect(self.ds_params_changed)
        self.ds_param_voltage_1.clicked.connect(self.ds_params_changed)
        self.ds_param_current_1.clicked.connect(self.ds_params_changed)
        self.ds_param_voltage_2.clicked.connect(self.ds_params_changed)
        self.ds_param_current_2.clicked.connect(self.ds_params_changed)
        self.sm_left_plot_settings.clicked.connect(self.sm_plot_1.show_plot_params_dialog)
        self.sm_right_plot_settings.clicked.connect(self.sm_plot_2.show_plot_params_dialog)
        self.ds_left_plot_settings.clicked.connect(self.ds_plot_1.show_plot_params_dialog)
        self.ds_right_plot_settings.clicked.connect(self.ds_plot_2.show_plot_params_dialog)

        # === Sweep parameter configuration change connections ===
        self.sm_param_sweep_voltage.clicked.connect(self.sm_params_changed)
        self.sm_param_sweep_current.clicked.connect(self.sm_params_changed)
        self.sm_param_constant_voltage.clicked.connect(self.sm_params_changed)
        self.sm_param_constant_current.clicked.connect(self.sm_params_changed)

        # === Menubar connections ===
        self.menubar_save_configuration.triggered.connect(self.save_configuration)
        self.menubar_load_configuration.triggered.connect(self.load_configuration)

    def get_sweep_parameters(self, quick_measurement=False):

        return SweepParameters(
            Source.VOLTAGE if self.sm_param_sweep_voltage.isChecked() else Source.CURRENT,
            self.sm_param_sweep_start.value(),
            self.sm_param_quick_sweep_step_override.value() if quick_measurement else self.sm_param_sweep_step.value(),
            self.sm_param_sweep_end.value(),
            self.sm_param_sweep_compliance.value(),
            Source.VOLTAGE if self.sm_param_constant_voltage.isChecked() else Source.CURRENT,
            self.sm_param_constant_start.value(),
            self.sm_param_constant_step.value(),
            self.sm_param_constant_end.value(),
            self.sm_param_constant_compliance.value(),
            self.sm_param_quick_pause_between_measurements.value() if quick_measurement else self.sm_param_pause_between_measurements.value(),
            self.sm_param_pause_between_sweeps.value(),
            1 if quick_measurement else self.sm_param_number_of_tests.value(),
        )

    def get_stream_parameters(self):

        measurement_duration = -1
        measurement_count = -1

        if self.ds_param_continuous.isChecked():
            measurement_mode = DatastreamMode.CONTINUOUS
        elif self.ds_param_fixed_duration.isChecked():
            measurement_mode = DatastreamMode.FIXED_DURATION
            measurement_duration = self.ds_param_duration.value()
        else:
            measurement_mode = DatastreamMode.FIXED_COUNT
            measurement_count = self.ds_param_number_of_measurements.value()

        return DatastreamParameters(
            Source.VOLTAGE if self.ds_param_voltage_1.isChecked() else Source.CURRENT,
            self.ds_param_output_1.value(),
            self.ds_param_compliance_1.value(),
            Source.VOLTAGE if self.ds_param_voltage_2.isChecked() else Source.CURRENT,
            self.ds_param_output_2.value(),
            self.ds_param_compliance_2.value(),
            measurement_mode,
            self.ds_param_pause_between_measurements.value(),
            measurement_duration,
            measurement_count,
        )

    def get_ds_metadata(self):
        light_dark = ""

        if self.ds_meta_light.isChecked():
            light_dark = "light"
        elif self.ds_meta_dark.isChecked():
            light_dark = "dark"

        return {
            "Wafer #": self.ds_meta_wafer.text(),
            "Chip #": self.ds_meta_chip.text(),
            "Step of the Process": self.ds_meta_step.text(),
            "Light/Dark":light_dark,
            "Date":datetime.now().strftime("%Y-%m-%d"),
            "Time":datetime.now().strftime("%H:%M:%S"),
            "Comments": self.ds_meta_comments.toPlainText(),
        }
        #     "SMU 1 Serial Number": self.ds_smu_select_1.currentText(),
        #     "SMU 2 Serial Number": self.ds_smu_select_2.currentText(),
        # }

    def get_sm_metadata(self):
        light_dark = ""

        if self.sm_meta_light.isChecked():
            light_dark = "light"
        elif self.sm_meta_dark.isChecked():
            light_dark = "dark"

        return {
            "Wafer #":self.sm_meta_wafer.text(),
            "Chip #":self.sm_meta_chip.text(),
            "Step of the Process":self.sm_meta_step.text(),
            "Light/Dark":light_dark,
            "Date":datetime.now().strftime("%Y-%m-%d"),
            "Time":datetime.now().strftime("%H:%M:%S"),
            "Comments":self.sm_meta_comments.toPlainText(),
        }
        #     "SMU 1 Serial Number":self.sm_sweep_smu_select.currentText(),
        #     "SMU 2 Serial Number":self.sm_constant_smu_select.currentText(),
        # }

    @QtCore.Slot()
    def ds_params_changed(self):

        # Update the input fields for measurement parameter input
        if self.ds_param_continuous.isChecked():
            self.ds_param_duration.setEnabled(False)
            self.ds_param_number_of_measurements.setEnabled(False)
        elif self.ds_param_fixed_number.isChecked():
            self.ds_param_duration.setEnabled(False)
            self.ds_param_number_of_measurements.setEnabled(True)
        elif self.ds_param_fixed_duration.isChecked():
            self.ds_param_duration.setEnabled(True)
            self.ds_param_number_of_measurements.setEnabled(False)

        # Change the suffixes for the inputs
        if self.ds_param_voltage_1.isChecked():
            self.ds_param_output_1.setSuffix(" V")
            self.ds_param_compliance_1.setSuffix(" A")
        else:
            self.ds_param_output_1.setSuffix(" A")
            self.ds_param_compliance_1.setSuffix(" V")

        if self.ds_param_voltage_2.isChecked():
            self.ds_param_output_2.setSuffix(" V")
            self.ds_param_compliance_2.setSuffix(" A")
        else:
            self.ds_param_output_2.setSuffix(" A")
            self.ds_param_compliance_2.setSuffix(" V")

    @QtCore.Slot()
    def sm_params_changed(self):

        # Change the suffixes for the inputs
        if self.sm_param_constant_voltage.isChecked():
            self.sm_param_constant_start.setSuffix(" V")
            self.sm_param_constant_step.setSuffix(" V")
            self.sm_param_constant_end.setSuffix(" V")
            self.sm_param_constant_compliance.setSuffix(" A")
        else:
            self.sm_param_constant_start.setSuffix(" A")
            self.sm_param_constant_step.setSuffix(" A")
            self.sm_param_constant_end.setSuffix(" A")
            self.sm_param_constant_compliance.setSuffix(" V")

        if self.sm_param_sweep_voltage.isChecked():
            self.sm_param_sweep_start.setSuffix(" V")
            self.sm_param_sweep_step.setSuffix(" V")
            self.sm_param_sweep_end.setSuffix(" V")
            self.sm_param_quick_sweep_step_override.setSuffix(" V")
            self.sm_param_sweep_compliance.setSuffix(" A")
        else:
            self.sm_param_sweep_start.setSuffix(" A")
            self.sm_param_sweep_step.setSuffix(" A")
            self.sm_param_sweep_end.setSuffix(" A")
            self.sm_param_quick_sweep_step_override.setSuffix(" A")
            self.sm_param_sweep_compliance.setSuffix(" V")

    @QtCore.Slot()
    def save_configuration(self):
        params = self.findChildren(QtWidgets.QWidget, QtCore.QRegularExpression("param"))

        config = {}

        # Params from ui elements
        for p in params:
            if isinstance(p, (QtWidgets.QSpinBox, QtWidgets.QDoubleSpinBox)):
                config[p.objectName()] = p.value()
            elif isinstance(p, (QtWidgets.QRadioButton, QtWidgets.QCheckBox)):
                config[p.objectName()] = p.isChecked()

        # Plot params
        config["sm_plot_1.x_param"] = self.sm_plot_1.x_param.name
        config["sm_plot_1.y_param"] = self.sm_plot_1.y_param.name
        config["sm_plot_2.x_param"] = self.sm_plot_2.x_param.name
        config["sm_plot_2.y_param"] = self.sm_plot_2.y_param.name
        config["ds_plot_1.x_param"] = self.ds_plot_1.x_param.name
        config["ds_plot_1.y_param"] = self.ds_plot_1.y_param.name
        config["ds_plot_2.x_param"] = self.ds_plot_2.x_param.name
        config["ds_plot_2.y_param"] = self.ds_plot_2.y_param.name
        config["data_plot.x_param"] = self.data_plot.x_param.name
        config["data_plot.y_param"] = self.data_plot.y_param.name

        # See where the user wants to save the file
        path, _ = QtWidgets.QFileDialog(self).getSaveFileName(self, filter="*.json", dir="config_default.json")

        if path == "":
            return

        # Write the config to disk
        with open(path, "w") as fp:
            json.dump(config, fp, indent=4)

    @QtCore.Slot()
    def load_configuration(self):
        # See what file the user wants to load
        path, _ = QtWidgets.QFileDialog(self).getOpenFileName(self, filter="*.json")

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
                parent=self,
            ).show()
            return

        # Apply those values
        for object_name, value in config.items():
            c: QtWidgets.QWidget = self.findChild(QtWidgets.QWidget, object_name)

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
            self.sm_plot_1.set_plot_parameters(PlotParam(config["sm_plot_1.x_param"]), PlotParam(config["sm_plot_1.y_param"]))
            self.sm_plot_2.set_plot_parameters(PlotParam(config["sm_plot_2.x_param"]), PlotParam(config["sm_plot_2.y_param"]))
            self.ds_plot_1.set_plot_parameters(PlotParam(config["ds_plot_1.x_param"]), PlotParam(config["ds_plot_1.y_param"]))
            self.ds_plot_2.set_plot_parameters(PlotParam(config["ds_plot_2.x_param"]), PlotParam(config["ds_plot_2.y_param"]))
            self.data_plot.set_plot_parameters(PlotParam(config["data_plot.x_param"]), PlotParam(config["data_plot.y_param"]))
        except KeyError:
            pass

    def closeEvent(self, event):
        # TODO: Check to save before closing
        event.accept()
        # do stuff
        # if self.check_unsaved_data():
        #     event.accept() # let the window close
        # else:
        #     event.ignore()


if __name__ == "__main__":

    import sys

    from PySide6.QtWidgets import QApplication

    # Create the application instance
    app = QApplication(sys.argv)

    ui = MainWindow()
    ui.show()

    # Enter the main event loop
    sys.exit(app.exec())
