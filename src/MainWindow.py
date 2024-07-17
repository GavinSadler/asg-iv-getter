from datetime import datetime

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from Measurement import DatastreamMode, DatastreamParameters, SweepParameters
from SourceMeter import Source
from UserInterface.ui_main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)

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

        self.sm_params_changed()
        self.ds_params_changed()

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
            self.sm_param_repeat_sweep.isChecked(),
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
            "Light/Dark": light_dark,
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Time": datetime.now().strftime("%H:%M:%S"),
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
            "Wafer #": self.sm_meta_wafer.text(),
            "Chip #": self.sm_meta_chip.text(),
            "Step of the Process": self.sm_meta_step.text(),
            "Light/Dark": light_dark,
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Comments": self.sm_meta_comments.toPlainText(),
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
            set_input_mode(self.ds_param_output_1, False, False, Source.VOLTAGE)
            set_input_mode(self.ds_param_compliance_1, False, True, Source.CURRENT)
        else:
            set_input_mode(self.ds_param_output_1, False, False, Source.CURRENT)
            set_input_mode(self.ds_param_compliance_1, False, True, Source.VOLTAGE)

        if self.ds_param_voltage_2.isChecked():
            set_input_mode(self.ds_param_output_2, False, False, Source.VOLTAGE)
            set_input_mode(self.ds_param_compliance_2, False, True, Source.CURRENT)
        else:
            set_input_mode(self.ds_param_output_2, False, False, Source.CURRENT)
            set_input_mode(self.ds_param_compliance_2, False, True, Source.VOLTAGE)

    @QtCore.Slot()
    def sm_params_changed(self):

        # Change the suffixes for the inputs
        if self.sm_param_constant_voltage.isChecked():
            set_input_mode(self.sm_param_constant_start, False, False, Source.VOLTAGE)
            set_input_mode(self.sm_param_constant_step, True, False, Source.VOLTAGE)
            set_input_mode(self.sm_param_constant_end, False, False, Source.VOLTAGE)
            set_input_mode(self.sm_param_constant_compliance, False, True, Source.CURRENT)
        else:
            set_input_mode(self.sm_param_constant_start, False, False, Source.CURRENT)
            set_input_mode(self.sm_param_constant_step, True, False, Source.CURRENT)
            set_input_mode(self.sm_param_constant_end, False, False, Source.CURRENT)
            set_input_mode(self.sm_param_constant_compliance, False, True, Source.VOLTAGE)

        if self.sm_param_sweep_voltage.isChecked():
            set_input_mode(self.sm_param_sweep_start, False, False, Source.VOLTAGE)
            set_input_mode(self.sm_param_sweep_step, True, False, Source.VOLTAGE)
            set_input_mode(self.sm_param_sweep_end, False, False, Source.VOLTAGE)
            set_input_mode(self.sm_param_quick_sweep_step_override, True, False, Source.VOLTAGE)
            set_input_mode(self.sm_param_sweep_compliance, False, True, Source.CURRENT)
        else:
            set_input_mode(self.sm_param_sweep_start, False, False, Source.CURRENT)
            set_input_mode(self.sm_param_sweep_step, True, False, Source.CURRENT)
            set_input_mode(self.sm_param_sweep_end, False, False, Source.CURRENT)
            set_input_mode(self.sm_param_quick_sweep_step_override, True, False, Source.CURRENT)
            set_input_mode(self.sm_param_sweep_compliance, False, True, Source.VOLTAGE)

    def closeEvent(self, event):
        # TODO: Check to save before closing
        event.accept()
        # do stuff
        # if self.check_unsaved_data():
        #     event.accept() # let the window close
        # else:
        #     event.ignore()


def set_input_mode(input: QtWidgets.QDoubleSpinBox, is_step: bool, is_compliance: bool, source: Source):

    if source is Source.VOLTAGE:
        input.setMaximum(1100)
        input.setMinimum(-1100)
        input.setSuffix(" V")
        input.setDecimals(6)

        if is_compliance:
            input.setMaximum(210)
            input.setMinimum(0)

        if is_step:
            input.setMinimum(0.000001)

    else:
        input.setMaximum(1000)
        input.setMinimum(-1000)
        input.setSuffix(" mA")
        input.setDecimals(9)

        if is_compliance:
            input.setMaximum(1050)
            input.setMinimum(0)

        if is_step:
            input.setMinimum(0.000000001)


if __name__ == "__main__":

    import sys

    from PySide6.QtWidgets import QApplication

    # Create the application instance
    app = QApplication(sys.argv)

    ui = MainWindow()
    ui.show()

    # Enter the main event loop
    sys.exit(app.exec())
