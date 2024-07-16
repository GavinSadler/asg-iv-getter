# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowXqkgmu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMenu,
    QMenuBar,
    QPlainTextEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpinBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from DataPlot import DataPlot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 850)
        MainWindow.setMinimumSize(QSize(900, 850))
        self.menubar_sourcemeter_connections = QAction(MainWindow)
        self.menubar_sourcemeter_connections.setObjectName("menubar_sourcemeter_connections")
        self.menubar_save_configuration = QAction(MainWindow)
        self.menubar_save_configuration.setObjectName("menubar_save_configuration")
        self.menubar_load_configuration = QAction(MainWindow)
        self.menubar_load_configuration.setObjectName("menubar_load_configuration")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sweep_measurement = QWidget()
        self.tab_sweep_measurement.setObjectName("tab_sweep_measurement")
        self.gridLayout = QGridLayout(self.tab_sweep_measurement)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QGroupBox(self.tab_sweep_measurement)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(425, 0))
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 2, 1, 1)

        self.sm_meta_light = QRadioButton(self.groupBox_3)
        self.sm_meta_light.setObjectName("sm_meta_light")

        self.gridLayout_3.addWidget(self.sm_meta_light, 1, 4, 1, 1)

        self.sm_meta_step = QLineEdit(self.groupBox_3)
        self.sm_meta_step.setObjectName("sm_meta_step")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sm_meta_step.sizePolicy().hasHeightForWidth())
        self.sm_meta_step.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.sm_meta_step, 1, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")

        self.gridLayout_3.addWidget(self.label_14, 1, 2, 1, 1)

        self.sm_meta_chip = QLineEdit(self.groupBox_3)
        self.sm_meta_chip.setObjectName("sm_meta_chip")
        sizePolicy.setHeightForWidth(self.sm_meta_chip.sizePolicy().hasHeightForWidth())
        self.sm_meta_chip.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.sm_meta_chip, 0, 3, 1, 2)

        self.sm_meta_dark = QRadioButton(self.groupBox_3)
        self.sm_meta_dark.setObjectName("sm_meta_dark")

        self.gridLayout_3.addWidget(self.sm_meta_dark, 1, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName("label_15")

        self.gridLayout_3.addWidget(self.label_15, 3, 0, 1, 1)

        self.sm_meta_comments = QPlainTextEdit(self.groupBox_3)
        self.sm_meta_comments.setObjectName("sm_meta_comments")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sm_meta_comments.sizePolicy().hasHeightForWidth())
        self.sm_meta_comments.setSizePolicy(sizePolicy1)
        self.sm_meta_comments.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_3.addWidget(self.sm_meta_comments, 3, 1, 1, 4)

        self.sm_meta_wafer = QLineEdit(self.groupBox_3)
        self.sm_meta_wafer.setObjectName("sm_meta_wafer")
        sizePolicy.setHeightForWidth(self.sm_meta_wafer.sizePolicy().hasHeightForWidth())
        self.sm_meta_wafer.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.sm_meta_wafer, 0, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)

        self.sm_meta_time_data = QCheckBox(self.groupBox_3)
        self.sm_meta_time_data.setObjectName("sm_meta_time_data")

        self.gridLayout_3.addWidget(self.sm_meta_time_data, 4, 1, 1, 1)

        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.sm_plot_1 = DataPlot(self.tab_sweep_measurement)
        self.sm_plot_1.setObjectName("sm_plot_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.sm_plot_1.sizePolicy().hasHeightForWidth())
        self.sm_plot_1.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.sm_plot_1, 3, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab_sweep_measurement)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setMinimumSize(QSize(425, 0))
        self.gridLayout_11 = QGridLayout(self.groupBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label_4, 2, 2, 1, 1)

        self.sm_param_sweep_end = QDoubleSpinBox(self.groupBox)
        self.sm_param_sweep_end.setObjectName("sm_param_sweep_end")
        self.sm_param_sweep_end.setDecimals(6)
        self.sm_param_sweep_end.setMinimum(-1000.000000000000000)
        self.sm_param_sweep_end.setMaximum(1000.000000000000000)
        self.sm_param_sweep_end.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_11.addWidget(self.sm_param_sweep_end, 3, 2, 1, 1)

        self.sm_param_sweep_start = QDoubleSpinBox(self.groupBox)
        self.sm_param_sweep_start.setObjectName("sm_param_sweep_start")
        self.sm_param_sweep_start.setDecimals(6)
        self.sm_param_sweep_start.setMinimum(-1000.000000000000000)
        self.sm_param_sweep_start.setMaximum(1000.000000000000000)
        self.sm_param_sweep_start.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_11.addWidget(self.sm_param_sweep_start, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName("label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label, 2, 0, 1, 1)

        self.sm_param_sweep_step = QDoubleSpinBox(self.groupBox)
        self.sm_param_sweep_step.setObjectName("sm_param_sweep_step")
        self.sm_param_sweep_step.setDecimals(6)
        self.sm_param_sweep_step.setMinimum(-1000.000000000000000)
        self.sm_param_sweep_step.setMaximum(1000.000000000000000)
        self.sm_param_sweep_step.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_11.addWidget(self.sm_param_sweep_step, 3, 1, 1, 1)

        self.sm_param_sweep_voltage = QRadioButton(self.groupBox)
        self.sm_param_sweep_voltage.setObjectName("sm_param_sweep_voltage")
        self.sm_param_sweep_voltage.setChecked(True)

        self.gridLayout_11.addWidget(self.sm_param_sweep_voltage, 1, 1, 1, 1)

        self.sm_param_sweep_current = QRadioButton(self.groupBox)
        self.sm_param_sweep_current.setObjectName("sm_param_sweep_current")

        self.gridLayout_11.addWidget(self.sm_param_sweep_current, 1, 2, 1, 1)

        self.sm_sweep_smu_select = QComboBox(self.groupBox)
        self.sm_sweep_smu_select.addItem("")
        self.sm_sweep_smu_select.setObjectName("sm_sweep_smu_select")

        self.gridLayout_11.addWidget(self.sm_sweep_smu_select, 0, 1, 1, 2)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")

        self.gridLayout_11.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")

        self.gridLayout_11.addWidget(self.label_17, 4, 0, 1, 1)

        self.sm_param_sweep_compliance = QDoubleSpinBox(self.groupBox)
        self.sm_param_sweep_compliance.setObjectName("sm_param_sweep_compliance")
        self.sm_param_sweep_compliance.setDecimals(6)
        self.sm_param_sweep_compliance.setMaximum(1000.000000000000000)
        self.sm_param_sweep_compliance.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_param_sweep_compliance.setValue(0.000000000000000)

        self.gridLayout_11.addWidget(self.sm_param_sweep_compliance, 4, 1, 1, 2)

        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.tab_sweep_measurement)
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(425, 0))
        self.gridLayout_9 = QGridLayout(self.groupBox_8)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.sm_left_plot_settings = QPushButton(self.groupBox_8)
        self.sm_left_plot_settings.setObjectName("sm_left_plot_settings")

        self.gridLayout_9.addWidget(self.sm_left_plot_settings, 3, 0, 1, 1)

        self.sm_abort = QPushButton(self.groupBox_8)
        self.sm_abort.setObjectName("sm_abort")
        self.sm_abort.setEnabled(False)

        self.gridLayout_9.addWidget(self.sm_abort, 2, 1, 1, 1)

        self.sm_file_output_path = QLabel(self.groupBox_8)
        self.sm_file_output_path.setObjectName("sm_file_output_path")

        self.gridLayout_9.addWidget(self.sm_file_output_path, 0, 1, 1, 1)

        self.sm_progress = QProgressBar(self.groupBox_8)
        self.sm_progress.setObjectName("sm_progress")
        self.sm_progress.setValue(0)
        self.sm_progress.setTextVisible(False)

        self.gridLayout_9.addWidget(self.sm_progress, 4, 0, 1, 2)

        self.sm_file_output = QPushButton(self.groupBox_8)
        self.sm_file_output.setObjectName("sm_file_output")

        self.gridLayout_9.addWidget(self.sm_file_output, 0, 0, 1, 1)

        self.sm_save_last_run = QPushButton(self.groupBox_8)
        self.sm_save_last_run.setObjectName("sm_save_last_run")
        self.sm_save_last_run.setEnabled(False)

        self.gridLayout_9.addWidget(self.sm_save_last_run, 2, 0, 1, 1)

        self.sm_right_plot_settings = QPushButton(self.groupBox_8)
        self.sm_right_plot_settings.setObjectName("sm_right_plot_settings")

        self.gridLayout_9.addWidget(self.sm_right_plot_settings, 3, 1, 1, 1)

        self.gridLayout.addWidget(self.groupBox_8, 0, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_sweep_measurement)
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(425, 0))
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.sm_run_full_measurement = QPushButton(self.groupBox_6)
        self.sm_run_full_measurement.setObjectName("sm_run_full_measurement")

        self.gridLayout_6.addWidget(self.sm_run_full_measurement, 3, 0, 1, 2)

        self.label_22 = QLabel(self.groupBox_6)
        self.label_22.setObjectName("label_22")

        self.gridLayout_6.addWidget(self.label_22, 0, 0, 1, 1)

        self.sm_param_pause_between_measurements = QDoubleSpinBox(self.groupBox_6)
        self.sm_param_pause_between_measurements.setObjectName("sm_param_pause_between_measurements")
        self.sm_param_pause_between_measurements.setDecimals(3)
        self.sm_param_pause_between_measurements.setMaximum(100.000000000000000)
        self.sm_param_pause_between_measurements.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_6.addWidget(self.sm_param_pause_between_measurements, 1, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_6)
        self.label_25.setObjectName("label_25")

        self.gridLayout_6.addWidget(self.label_25, 2, 0, 1, 1)

        self.sm_param_number_of_tests = QSpinBox(self.groupBox_6)
        self.sm_param_number_of_tests.setObjectName("sm_param_number_of_tests")
        self.sm_param_number_of_tests.setMaximum(100)
        self.sm_param_number_of_tests.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_param_number_of_tests.setValue(1)

        self.gridLayout_6.addWidget(self.sm_param_number_of_tests, 0, 1, 1, 1)

        self.sm_param_pause_between_sweeps = QDoubleSpinBox(self.groupBox_6)
        self.sm_param_pause_between_sweeps.setObjectName("sm_param_pause_between_sweeps")
        self.sm_param_pause_between_sweeps.setDecimals(3)
        self.sm_param_pause_between_sweeps.setMaximum(100.000000000000000)
        self.sm_param_pause_between_sweeps.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_6.addWidget(self.sm_param_pause_between_sweeps, 2, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_6)
        self.label_26.setObjectName("label_26")

        self.gridLayout_6.addWidget(self.label_26, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.groupBox_6, 2, 1, 1, 1)

        self.sm_plot_2 = DataPlot(self.tab_sweep_measurement)
        self.sm_plot_2.setObjectName("sm_plot_2")
        sizePolicy2.setHeightForWidth(self.sm_plot_2.sizePolicy().hasHeightForWidth())
        self.sm_plot_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.sm_plot_2, 3, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.tab_sweep_measurement)
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(425, 0))
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.sm_param_quick_sweep_step_override = QDoubleSpinBox(self.groupBox_7)
        self.sm_param_quick_sweep_step_override.setObjectName("sm_param_quick_sweep_step_override")
        self.sm_param_quick_sweep_step_override.setDecimals(6)
        self.sm_param_quick_sweep_step_override.setMaximum(1000.000000000000000)
        self.sm_param_quick_sweep_step_override.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_10.addWidget(self.sm_param_quick_sweep_step_override, 1, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_7)
        self.label_28.setObjectName("label_28")
        self.label_28.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_28, 1, 0, 1, 1)

        self.sm_run_quick_measurement = QPushButton(self.groupBox_7)
        self.sm_run_quick_measurement.setObjectName("sm_run_quick_measurement")

        self.gridLayout_10.addWidget(self.sm_run_quick_measurement, 2, 0, 1, 2)

        self.sm_param_quick_pause_between_measurements = QDoubleSpinBox(self.groupBox_7)
        self.sm_param_quick_pause_between_measurements.setObjectName("sm_param_quick_pause_between_measurements")
        self.sm_param_quick_pause_between_measurements.setDecimals(3)
        self.sm_param_quick_pause_between_measurements.setMaximum(100.000000000000000)
        self.sm_param_quick_pause_between_measurements.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_10.addWidget(self.sm_param_quick_pause_between_measurements, 0, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_7)
        self.label_29.setObjectName("label_29")

        self.gridLayout_10.addWidget(self.label_29, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.groupBox_7, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_sweep_measurement)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(425, 0))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sm_param_constant_voltage = QRadioButton(self.groupBox_2)
        self.sm_param_constant_voltage.setObjectName("sm_param_constant_voltage")
        self.sm_param_constant_voltage.setChecked(True)

        self.gridLayout_2.addWidget(self.sm_param_constant_voltage, 1, 1, 1, 1)

        self.sm_param_constant_start = QDoubleSpinBox(self.groupBox_2)
        self.sm_param_constant_start.setObjectName("sm_param_constant_start")
        self.sm_param_constant_start.setDecimals(6)
        self.sm_param_constant_start.setMinimum(-1000.000000000000000)
        self.sm_param_constant_start.setMaximum(1000.000000000000000)
        self.sm_param_constant_start.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_2.addWidget(self.sm_param_constant_start, 3, 0, 1, 1)

        self.sm_constant_smu_select = QComboBox(self.groupBox_2)
        self.sm_constant_smu_select.addItem("")
        self.sm_constant_smu_select.setObjectName("sm_constant_smu_select")

        self.gridLayout_2.addWidget(self.sm_constant_smu_select, 0, 1, 1, 2)

        self.sm_param_constant_compliance = QDoubleSpinBox(self.groupBox_2)
        self.sm_param_constant_compliance.setObjectName("sm_param_constant_compliance")
        self.sm_param_constant_compliance.setDecimals(6)
        self.sm_param_constant_compliance.setMaximum(1000.000000000000000)
        self.sm_param_constant_compliance.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_param_constant_compliance.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.sm_param_constant_compliance, 4, 1, 1, 2)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")

        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.sm_param_constant_current = QRadioButton(self.groupBox_2)
        self.sm_param_constant_current.setObjectName("sm_param_constant_current")

        self.gridLayout_2.addWidget(self.sm_param_constant_current, 1, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.sm_param_constant_step = QDoubleSpinBox(self.groupBox_2)
        self.sm_param_constant_step.setObjectName("sm_param_constant_step")
        self.sm_param_constant_step.setDecimals(6)
        self.sm_param_constant_step.setMinimum(-1000.000000000000000)
        self.sm_param_constant_step.setMaximum(1000.000000000000000)
        self.sm_param_constant_step.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_2.addWidget(self.sm_param_constant_step, 3, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)

        self.sm_param_constant_end = QDoubleSpinBox(self.groupBox_2)
        self.sm_param_constant_end.setObjectName("sm_param_constant_end")
        self.sm_param_constant_end.setDecimals(6)
        self.sm_param_constant_end.setMinimum(-1000.000000000000000)
        self.sm_param_constant_end.setMaximum(1000.000000000000000)
        self.sm_param_constant_end.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_2.addWidget(self.sm_param_constant_end, 3, 2, 1, 1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_16, 2, 2, 1, 1)

        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_sweep_measurement, "")
        self.tab_data_stream = QWidget()
        self.tab_data_stream.setObjectName("tab_data_stream")
        self.gridLayout_12 = QGridLayout(self.tab_data_stream)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.groupBox_5 = QGroupBox(self.tab_data_stream)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(425, 0))
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ds_meta_step = QLineEdit(self.groupBox_5)
        self.ds_meta_step.setObjectName("ds_meta_step")
        sizePolicy.setHeightForWidth(self.ds_meta_step.sizePolicy().hasHeightForWidth())
        self.ds_meta_step.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.ds_meta_step, 1, 1, 1, 1)

        self.ds_meta_light = QRadioButton(self.groupBox_5)
        self.ds_meta_light.setObjectName("ds_meta_light")

        self.gridLayout_5.addWidget(self.ds_meta_light, 1, 4, 1, 1)

        self.ds_meta_comments = QPlainTextEdit(self.groupBox_5)
        self.ds_meta_comments.setObjectName("ds_meta_comments")
        sizePolicy1.setHeightForWidth(self.ds_meta_comments.sizePolicy().hasHeightForWidth())
        self.ds_meta_comments.setSizePolicy(sizePolicy1)
        self.ds_meta_comments.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_5.addWidget(self.ds_meta_comments, 2, 1, 1, 4)

        self.label_34 = QLabel(self.groupBox_5)
        self.label_34.setObjectName("label_34")

        self.gridLayout_5.addWidget(self.label_34, 2, 0, 1, 1)

        self.ds_meta_chip = QLineEdit(self.groupBox_5)
        self.ds_meta_chip.setObjectName("ds_meta_chip")
        sizePolicy.setHeightForWidth(self.ds_meta_chip.sizePolicy().hasHeightForWidth())
        self.ds_meta_chip.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.ds_meta_chip, 0, 3, 1, 2)

        self.label_32 = QLabel(self.groupBox_5)
        self.label_32.setObjectName("label_32")

        self.gridLayout_5.addWidget(self.label_32, 1, 2, 1, 1)

        self.ds_meta_wafer = QLineEdit(self.groupBox_5)
        self.ds_meta_wafer.setObjectName("ds_meta_wafer")
        sizePolicy.setHeightForWidth(self.ds_meta_wafer.sizePolicy().hasHeightForWidth())
        self.ds_meta_wafer.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.ds_meta_wafer, 0, 1, 1, 1)

        self.ds_meta_dark = QRadioButton(self.groupBox_5)
        self.ds_meta_dark.setObjectName("ds_meta_dark")

        self.gridLayout_5.addWidget(self.ds_meta_dark, 1, 3, 1, 1)

        self.label_31 = QLabel(self.groupBox_5)
        self.label_31.setObjectName("label_31")

        self.gridLayout_5.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_30 = QLabel(self.groupBox_5)
        self.label_30.setObjectName("label_30")

        self.gridLayout_5.addWidget(self.label_30, 1, 0, 1, 1)

        self.label_33 = QLabel(self.groupBox_5)
        self.label_33.setObjectName("label_33")

        self.gridLayout_5.addWidget(self.label_33, 0, 2, 1, 1)

        self.ds_meta_time_data = QCheckBox(self.groupBox_5)
        self.ds_meta_time_data.setObjectName("ds_meta_time_data")

        self.gridLayout_5.addWidget(self.ds_meta_time_data, 3, 1, 1, 1)

        self.gridLayout_12.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.tab_data_stream)
        self.groupBox_15.setObjectName("groupBox_15")
        self.groupBox_15.setMinimumSize(QSize(425, 0))
        self.gridLayout_19 = QGridLayout(self.groupBox_15)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.ds_param_current_1 = QRadioButton(self.groupBox_15)
        self.ds_param_current_1.setObjectName("ds_param_current_1")

        self.gridLayout_19.addWidget(self.ds_param_current_1, 1, 2, 1, 1)

        self.label_53 = QLabel(self.groupBox_15)
        self.label_53.setObjectName("label_53")

        self.gridLayout_19.addWidget(self.label_53, 0, 0, 1, 1)

        self.label_54 = QLabel(self.groupBox_15)
        self.label_54.setObjectName("label_54")

        self.gridLayout_19.addWidget(self.label_54, 3, 0, 1, 1)

        self.ds_param_voltage_1 = QRadioButton(self.groupBox_15)
        self.ds_param_voltage_1.setObjectName("ds_param_voltage_1")
        self.ds_param_voltage_1.setChecked(True)

        self.gridLayout_19.addWidget(self.ds_param_voltage_1, 1, 1, 1, 1)

        self.ds_smu_select_1 = QComboBox(self.groupBox_15)
        self.ds_smu_select_1.addItem("")
        self.ds_smu_select_1.setObjectName("ds_smu_select_1")

        self.gridLayout_19.addWidget(self.ds_smu_select_1, 0, 1, 1, 2)

        self.label_55 = QLabel(self.groupBox_15)
        self.label_55.setObjectName("label_55")

        self.gridLayout_19.addWidget(self.label_55, 1, 0, 1, 1)

        self.ds_param_compliance_1 = QDoubleSpinBox(self.groupBox_15)
        self.ds_param_compliance_1.setObjectName("ds_param_compliance_1")
        self.ds_param_compliance_1.setDecimals(6)
        self.ds_param_compliance_1.setMinimum(0.000000000000000)
        self.ds_param_compliance_1.setMaximum(1000.000000000000000)
        self.ds_param_compliance_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_19.addWidget(self.ds_param_compliance_1, 3, 1, 1, 2)

        self.label_56 = QLabel(self.groupBox_15)
        self.label_56.setObjectName("label_56")

        self.gridLayout_19.addWidget(self.label_56, 2, 0, 1, 1)

        self.ds_param_output_1 = QDoubleSpinBox(self.groupBox_15)
        self.ds_param_output_1.setObjectName("ds_param_output_1")
        self.ds_param_output_1.setDecimals(6)
        self.ds_param_output_1.setMinimum(-1000.000000000000000)
        self.ds_param_output_1.setMaximum(1000.000000000000000)
        self.ds_param_output_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_19.addWidget(self.ds_param_output_1, 2, 1, 1, 2)

        self.gridLayout_12.addWidget(self.groupBox_15, 3, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.tab_data_stream)
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_24 = QGridLayout(self.groupBox_20)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.ds_param_fixed_duration = QRadioButton(self.groupBox_20)
        self.ds_param_fixed_duration.setObjectName("ds_param_fixed_duration")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ds_param_fixed_duration.sizePolicy().hasHeightForWidth())
        self.ds_param_fixed_duration.setSizePolicy(sizePolicy4)

        self.gridLayout_24.addWidget(self.ds_param_fixed_duration, 2, 0, 1, 1)

        self.label_73 = QLabel(self.groupBox_20)
        self.label_73.setObjectName("label_73")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy5)

        self.gridLayout_24.addWidget(self.label_73, 0, 2, 1, 1)

        self.ds_param_fixed_number = QRadioButton(self.groupBox_20)
        self.ds_param_fixed_number.setObjectName("ds_param_fixed_number")
        sizePolicy4.setHeightForWidth(self.ds_param_fixed_number.sizePolicy().hasHeightForWidth())
        self.ds_param_fixed_number.setSizePolicy(sizePolicy4)

        self.gridLayout_24.addWidget(self.ds_param_fixed_number, 1, 0, 1, 1)

        self.ds_param_duration = QDoubleSpinBox(self.groupBox_20)
        self.ds_param_duration.setObjectName("ds_param_duration")
        self.ds_param_duration.setEnabled(False)
        self.ds_param_duration.setDecimals(3)
        self.ds_param_duration.setMaximum(100.000000000000000)
        self.ds_param_duration.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_24.addWidget(self.ds_param_duration, 0, 3, 1, 1)

        self.ds_param_continuous = QRadioButton(self.groupBox_20)
        self.ds_param_continuous.setObjectName("ds_param_continuous")
        sizePolicy4.setHeightForWidth(self.ds_param_continuous.sizePolicy().hasHeightForWidth())
        self.ds_param_continuous.setSizePolicy(sizePolicy4)
        self.ds_param_continuous.setChecked(True)

        self.gridLayout_24.addWidget(self.ds_param_continuous, 0, 0, 1, 1)

        self.line_3 = QFrame(self.groupBox_20)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_24.addWidget(self.line_3, 0, 1, 3, 1)

        self.label_74 = QLabel(self.groupBox_20)
        self.label_74.setObjectName("label_74")
        sizePolicy5.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy5)

        self.gridLayout_24.addWidget(self.label_74, 2, 2, 1, 1)

        self.ds_param_pause_between_measurements = QDoubleSpinBox(self.groupBox_20)
        self.ds_param_pause_between_measurements.setObjectName("ds_param_pause_between_measurements")
        self.ds_param_pause_between_measurements.setDecimals(3)
        self.ds_param_pause_between_measurements.setMaximum(100.000000000000000)
        self.ds_param_pause_between_measurements.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_24.addWidget(self.ds_param_pause_between_measurements, 2, 3, 1, 1)

        self.label_75 = QLabel(self.groupBox_20)
        self.label_75.setObjectName("label_75")
        sizePolicy5.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy5)

        self.gridLayout_24.addWidget(self.label_75, 1, 2, 1, 1)

        self.ds_param_number_of_measurements = QSpinBox(self.groupBox_20)
        self.ds_param_number_of_measurements.setObjectName("ds_param_number_of_measurements")
        self.ds_param_number_of_measurements.setEnabled(False)
        self.ds_param_number_of_measurements.setMaximum(100)
        self.ds_param_number_of_measurements.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_24.addWidget(self.ds_param_number_of_measurements, 1, 3, 1, 1)

        self.gridLayout_12.addWidget(self.groupBox_20, 2, 0, 1, 1)

        self.groupBox_19 = QGroupBox(self.tab_data_stream)
        self.groupBox_19.setObjectName("groupBox_19")
        self.groupBox_19.setMinimumSize(QSize(425, 0))
        self.gridLayout_23 = QGridLayout(self.groupBox_19)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.ds_param_current_2 = QRadioButton(self.groupBox_19)
        self.ds_param_current_2.setObjectName("ds_param_current_2")

        self.gridLayout_23.addWidget(self.ds_param_current_2, 1, 2, 1, 1)

        self.label_69 = QLabel(self.groupBox_19)
        self.label_69.setObjectName("label_69")

        self.gridLayout_23.addWidget(self.label_69, 0, 0, 1, 1)

        self.label_70 = QLabel(self.groupBox_19)
        self.label_70.setObjectName("label_70")

        self.gridLayout_23.addWidget(self.label_70, 3, 0, 1, 1)

        self.ds_param_voltage_2 = QRadioButton(self.groupBox_19)
        self.ds_param_voltage_2.setObjectName("ds_param_voltage_2")
        self.ds_param_voltage_2.setChecked(True)

        self.gridLayout_23.addWidget(self.ds_param_voltage_2, 1, 1, 1, 1)

        self.ds_smu_select_2 = QComboBox(self.groupBox_19)
        self.ds_smu_select_2.addItem("")
        self.ds_smu_select_2.setObjectName("ds_smu_select_2")

        self.gridLayout_23.addWidget(self.ds_smu_select_2, 0, 1, 1, 2)

        self.label_71 = QLabel(self.groupBox_19)
        self.label_71.setObjectName("label_71")

        self.gridLayout_23.addWidget(self.label_71, 1, 0, 1, 1)

        self.ds_param_compliance_2 = QDoubleSpinBox(self.groupBox_19)
        self.ds_param_compliance_2.setObjectName("ds_param_compliance_2")
        self.ds_param_compliance_2.setDecimals(6)
        self.ds_param_compliance_2.setMinimum(0.000000000000000)
        self.ds_param_compliance_2.setMaximum(1000.000000000000000)
        self.ds_param_compliance_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_23.addWidget(self.ds_param_compliance_2, 3, 1, 1, 2)

        self.label_72 = QLabel(self.groupBox_19)
        self.label_72.setObjectName("label_72")

        self.gridLayout_23.addWidget(self.label_72, 2, 0, 1, 1)

        self.ds_param_output_2 = QDoubleSpinBox(self.groupBox_19)
        self.ds_param_output_2.setObjectName("ds_param_output_2")
        self.ds_param_output_2.setDecimals(6)
        self.ds_param_output_2.setMinimum(-1000.000000000000000)
        self.ds_param_output_2.setMaximum(1000.000000000000000)
        self.ds_param_output_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_23.addWidget(self.ds_param_output_2, 2, 1, 1, 2)

        self.gridLayout_12.addWidget(self.groupBox_19, 3, 1, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_data_stream)
        self.groupBox_14.setObjectName("groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(425, 0))
        self.gridLayout_18 = QGridLayout(self.groupBox_14)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.ds_file_output = QPushButton(self.groupBox_14)
        self.ds_file_output.setObjectName("ds_file_output")

        self.gridLayout_18.addWidget(self.ds_file_output, 0, 0, 1, 1)

        self.ds_progress = QProgressBar(self.groupBox_14)
        self.ds_progress.setObjectName("ds_progress")
        self.ds_progress.setValue(0)
        self.ds_progress.setTextVisible(False)

        self.gridLayout_18.addWidget(self.ds_progress, 3, 0, 1, 2)

        self.ds_file_output_path = QLabel(self.groupBox_14)
        self.ds_file_output_path.setObjectName("ds_file_output_path")

        self.gridLayout_18.addWidget(self.ds_file_output_path, 0, 1, 1, 1)

        self.ds_save_last_run = QPushButton(self.groupBox_14)
        self.ds_save_last_run.setObjectName("ds_save_last_run")
        self.ds_save_last_run.setEnabled(False)

        self.gridLayout_18.addWidget(self.ds_save_last_run, 1, 0, 1, 1)

        self.ds_stream = QPushButton(self.groupBox_14)
        self.ds_stream.setObjectName("ds_stream")
        self.ds_stream.setEnabled(True)

        self.gridLayout_18.addWidget(self.ds_stream, 1, 1, 1, 1)

        self.ds_left_plot_settings = QPushButton(self.groupBox_14)
        self.ds_left_plot_settings.setObjectName("ds_left_plot_settings")

        self.gridLayout_18.addWidget(self.ds_left_plot_settings, 2, 0, 1, 1)

        self.ds_right_plot_settings = QPushButton(self.groupBox_14)
        self.ds_right_plot_settings.setObjectName("ds_right_plot_settings")

        self.gridLayout_18.addWidget(self.ds_right_plot_settings, 2, 1, 1, 1)

        self.gridLayout_12.addWidget(self.groupBox_14, 0, 1, 1, 1)

        self.ds_plot_1 = DataPlot(self.tab_data_stream)
        self.ds_plot_1.setObjectName("ds_plot_1")
        sizePolicy2.setHeightForWidth(self.ds_plot_1.sizePolicy().hasHeightForWidth())
        self.ds_plot_1.setSizePolicy(sizePolicy2)

        self.gridLayout_12.addWidget(self.ds_plot_1, 5, 0, 1, 1)

        self.ds_plot_2 = DataPlot(self.tab_data_stream)
        self.ds_plot_2.setObjectName("ds_plot_2")
        sizePolicy2.setHeightForWidth(self.ds_plot_2.sizePolicy().hasHeightForWidth())
        self.ds_plot_2.setSizePolicy(sizePolicy2)

        self.gridLayout_12.addWidget(self.ds_plot_2, 5, 1, 1, 1)

        self.tabWidget.addTab(self.tab_data_stream, "")
        self.tab_data_view = QWidget()
        self.tab_data_view.setObjectName("tab_data_view")
        self.gridLayout_7 = QGridLayout(self.tab_data_view)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.data_plot = DataPlot(self.tab_data_view)
        self.data_plot.setObjectName("data_plot")

        self.gridLayout_7.addWidget(self.data_plot, 0, 0, 1, 2)

        self.groupBox_9 = QGroupBox(self.tab_data_view)
        self.groupBox_9.setObjectName("groupBox_9")
        sizePolicy3.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy3)
        self.verticalLayout = QVBoxLayout(self.groupBox_9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sweep_measurements = QListWidget(self.groupBox_9)
        self.sweep_measurements.setObjectName("sweep_measurements")
        self.sweep_measurements.setMaximumSize(QSize(16777215, 200))
        self.sweep_measurements.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.sweep_measurements)

        self.gridLayout_7.addWidget(self.groupBox_9, 2, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.tab_data_view)
        self.groupBox_10.setObjectName("groupBox_10")
        sizePolicy3.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.datastream_measurements = QListWidget(self.groupBox_10)
        self.datastream_measurements.setObjectName("datastream_measurements")
        self.datastream_measurements.setMaximumSize(QSize(16777215, 200))
        self.datastream_measurements.setAlternatingRowColors(True)

        self.verticalLayout_2.addWidget(self.datastream_measurements)

        self.gridLayout_7.addWidget(self.groupBox_10, 2, 1, 1, 1)

        self.plot_parameters = QPushButton(self.tab_data_view)
        self.plot_parameters.setObjectName("plot_parameters")

        self.gridLayout_7.addWidget(self.plot_parameters, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_data_view, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 900, 22))
        self.menuTools = QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.sm_meta_wafer, self.sm_meta_chip)
        QWidget.setTabOrder(self.sm_meta_chip, self.sm_meta_step)
        QWidget.setTabOrder(self.sm_meta_step, self.sm_meta_dark)
        QWidget.setTabOrder(self.sm_meta_dark, self.sm_meta_light)
        QWidget.setTabOrder(self.sm_meta_light, self.sm_meta_comments)
        QWidget.setTabOrder(self.sm_meta_comments, self.sm_sweep_smu_select)
        QWidget.setTabOrder(self.sm_sweep_smu_select, self.sm_param_sweep_voltage)
        QWidget.setTabOrder(self.sm_param_sweep_voltage, self.sm_param_sweep_current)
        QWidget.setTabOrder(self.sm_param_sweep_current, self.sm_param_sweep_start)
        QWidget.setTabOrder(self.sm_param_sweep_start, self.sm_param_sweep_step)
        QWidget.setTabOrder(self.sm_param_sweep_step, self.sm_param_sweep_end)
        QWidget.setTabOrder(self.sm_param_sweep_end, self.sm_param_sweep_compliance)
        QWidget.setTabOrder(self.sm_param_sweep_compliance, self.sm_constant_smu_select)
        QWidget.setTabOrder(self.sm_constant_smu_select, self.sm_param_constant_voltage)
        QWidget.setTabOrder(self.sm_param_constant_voltage, self.sm_param_constant_current)
        QWidget.setTabOrder(self.sm_param_constant_current, self.sm_param_constant_compliance)
        QWidget.setTabOrder(self.sm_param_constant_compliance, self.sm_param_quick_pause_between_measurements)
        QWidget.setTabOrder(self.sm_param_quick_pause_between_measurements, self.sm_param_quick_sweep_step_override)
        QWidget.setTabOrder(self.sm_param_quick_sweep_step_override, self.sm_param_number_of_tests)
        QWidget.setTabOrder(self.sm_param_number_of_tests, self.sm_param_pause_between_measurements)
        QWidget.setTabOrder(self.sm_param_pause_between_measurements, self.sm_param_pause_between_sweeps)
        QWidget.setTabOrder(self.sm_param_pause_between_sweeps, self.sm_run_quick_measurement)
        QWidget.setTabOrder(self.sm_run_quick_measurement, self.sm_run_full_measurement)
        QWidget.setTabOrder(self.sm_run_full_measurement, self.sm_file_output)
        QWidget.setTabOrder(self.sm_file_output, self.sm_save_last_run)
        QWidget.setTabOrder(self.sm_save_last_run, self.sm_abort)
        QWidget.setTabOrder(self.sm_abort, self.sm_left_plot_settings)
        QWidget.setTabOrder(self.sm_left_plot_settings, self.sm_right_plot_settings)
        QWidget.setTabOrder(self.sm_right_plot_settings, self.ds_meta_wafer)
        QWidget.setTabOrder(self.ds_meta_wafer, self.ds_meta_chip)
        QWidget.setTabOrder(self.ds_meta_chip, self.ds_meta_step)
        QWidget.setTabOrder(self.ds_meta_step, self.ds_meta_dark)
        QWidget.setTabOrder(self.ds_meta_dark, self.ds_meta_light)
        QWidget.setTabOrder(self.ds_meta_light, self.ds_meta_comments)
        QWidget.setTabOrder(self.ds_meta_comments, self.ds_param_continuous)
        QWidget.setTabOrder(self.ds_param_continuous, self.ds_param_fixed_number)
        QWidget.setTabOrder(self.ds_param_fixed_number, self.ds_param_fixed_duration)
        QWidget.setTabOrder(self.ds_param_fixed_duration, self.ds_param_duration)
        QWidget.setTabOrder(self.ds_param_duration, self.ds_param_number_of_measurements)
        QWidget.setTabOrder(self.ds_param_number_of_measurements, self.ds_param_pause_between_measurements)
        QWidget.setTabOrder(self.ds_param_pause_between_measurements, self.ds_smu_select_1)
        QWidget.setTabOrder(self.ds_smu_select_1, self.ds_param_voltage_1)
        QWidget.setTabOrder(self.ds_param_voltage_1, self.ds_param_current_1)
        QWidget.setTabOrder(self.ds_param_current_1, self.ds_param_output_1)
        QWidget.setTabOrder(self.ds_param_output_1, self.ds_param_compliance_1)
        QWidget.setTabOrder(self.ds_param_compliance_1, self.ds_smu_select_2)
        QWidget.setTabOrder(self.ds_smu_select_2, self.ds_param_voltage_2)
        QWidget.setTabOrder(self.ds_param_voltage_2, self.ds_param_current_2)
        QWidget.setTabOrder(self.ds_param_current_2, self.ds_param_output_2)
        QWidget.setTabOrder(self.ds_param_output_2, self.ds_param_compliance_2)
        QWidget.setTabOrder(self.ds_param_compliance_2, self.ds_file_output)
        QWidget.setTabOrder(self.ds_file_output, self.ds_save_last_run)
        QWidget.setTabOrder(self.ds_save_last_run, self.ds_stream)
        QWidget.setTabOrder(self.ds_stream, self.ds_left_plot_settings)
        QWidget.setTabOrder(self.ds_left_plot_settings, self.ds_right_plot_settings)
        QWidget.setTabOrder(self.ds_right_plot_settings, self.tabWidget)

        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuTools.addAction(self.menubar_sourcemeter_connections)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.menubar_save_configuration)
        self.menuTools.addAction(self.menubar_load_configuration)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Dual SMU Controller", None))
        self.menubar_sourcemeter_connections.setText(QCoreApplication.translate("MainWindow", "Sourcemeter Connections", None))
        self.menubar_save_configuration.setText(QCoreApplication.translate("MainWindow", "Save Configuration", None))
        self.menubar_load_configuration.setText(QCoreApplication.translate("MainWindow", "Load Configuration", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", "Metadata", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", "Chip #:", None))
        self.sm_meta_light.setText(QCoreApplication.translate("MainWindow", "Light", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", "Light:", None))
        self.sm_meta_dark.setText(QCoreApplication.translate("MainWindow", "Dark", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", "Comments:", None))
        self.sm_meta_comments.setPlaceholderText(QCoreApplication.translate("MainWindow", "Enter comments here...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", "Wafer #:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", "Step of Process:", None))
        self.sm_meta_time_data.setText(QCoreApplication.translate("MainWindow", "Include time data?", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", "Sweep Parameters", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Step", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "End", None))
        self.sm_param_sweep_end.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.sm_param_sweep_start.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Start", None))
        self.sm_param_sweep_step.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.sm_param_sweep_voltage.setText(QCoreApplication.translate("MainWindow", "Voltage", None))
        self.sm_param_sweep_current.setText(QCoreApplication.translate("MainWindow", "Current", None))
        self.sm_sweep_smu_select.setItemText(0, QCoreApplication.translate("MainWindow", "Simulated", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", "Sourcemeter (smu_1):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "Mode:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", "Compliance:", None))
        self.sm_param_sweep_compliance.setSuffix(QCoreApplication.translate("MainWindow", " A", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", "Data", None))
        self.sm_left_plot_settings.setText(QCoreApplication.translate("MainWindow", "Left Plot Settings", None))
        self.sm_abort.setText(QCoreApplication.translate("MainWindow", "Abort Measurement", None))
        self.sm_file_output_path.setText(QCoreApplication.translate("MainWindow", "No data save location specified", None))
        self.sm_file_output.setText(QCoreApplication.translate("MainWindow", "File Output", None))
        self.sm_save_last_run.setText(QCoreApplication.translate("MainWindow", "Save Last Run", None))
        self.sm_right_plot_settings.setText(QCoreApplication.translate("MainWindow", "Right Plot Settings", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", "Full Measurement", None))
        self.sm_run_full_measurement.setText(QCoreApplication.translate("MainWindow", "Run Full Measurement", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", "Number of Tests:", None))
        self.sm_param_pause_between_measurements.setSuffix(QCoreApplication.translate("MainWindow", " sec", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", "Pause Between Sweeps:", None))
        self.sm_param_pause_between_sweeps.setSuffix(QCoreApplication.translate("MainWindow", " sec", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", "Pause Between Measurements:", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", "Quick Measurement", None))
        self.sm_param_quick_sweep_step_override.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", "Sweep Step Override:", None))
        self.sm_run_quick_measurement.setText(QCoreApplication.translate("MainWindow", "Run Quick Measurement", None))
        self.sm_param_quick_pause_between_measurements.setSuffix(QCoreApplication.translate("MainWindow", " sec", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", "Pause Between Measurements:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", "Constant Parameters", None))
        self.sm_param_constant_voltage.setText(QCoreApplication.translate("MainWindow", "Voltage", None))
        self.sm_param_constant_start.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.sm_constant_smu_select.setItemText(0, QCoreApplication.translate("MainWindow", "Simulated", None))

        self.sm_param_constant_compliance.setSuffix(QCoreApplication.translate("MainWindow", " A", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", "Compliance:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", "Sourcemeter (smu_2):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", "Mode:", None))
        self.sm_param_constant_current.setText(QCoreApplication.translate("MainWindow", "Current", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Start", None))
        self.sm_param_constant_step.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Step", None))
        self.sm_param_constant_end.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", "End", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sweep_measurement), QCoreApplication.translate("MainWindow", "Sweep Measurement", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", "Metadata", None))
        self.ds_meta_light.setText(QCoreApplication.translate("MainWindow", "Light", None))
        self.ds_meta_comments.setPlaceholderText(QCoreApplication.translate("MainWindow", "Enter comments here...", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", "Comments:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", "Light:", None))
        self.ds_meta_dark.setText(QCoreApplication.translate("MainWindow", "Dark", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", "Wafer #:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", "Step of Process:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", "Chip #:", None))
        self.ds_meta_time_data.setText(QCoreApplication.translate("MainWindow", "Include time data?", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", "SMU 1", None))
        self.ds_param_current_1.setText(QCoreApplication.translate("MainWindow", "Current", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", "Sourcemeter:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", "Compliance:", None))
        self.ds_param_voltage_1.setText(QCoreApplication.translate("MainWindow", "Voltage", None))
        self.ds_smu_select_1.setItemText(0, QCoreApplication.translate("MainWindow", "Simulated", None))

        self.label_55.setText(QCoreApplication.translate("MainWindow", "Mode:", None))
        self.ds_param_compliance_1.setSuffix(QCoreApplication.translate("MainWindow", " A", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", "Output:", None))
        self.ds_param_output_1.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", "Streaming Mode", None))
        self.ds_param_fixed_duration.setText(QCoreApplication.translate("MainWindow", "Fixed Duration", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", "Duration:", None))
        self.ds_param_fixed_number.setText(QCoreApplication.translate("MainWindow", "Fixed Number", None))
        self.ds_param_duration.setSuffix(QCoreApplication.translate("MainWindow", " sec", None))
        self.ds_param_continuous.setText(QCoreApplication.translate("MainWindow", "Continuous", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", "Pause Between Measurements:", None))
        self.ds_param_pause_between_measurements.setSuffix(QCoreApplication.translate("MainWindow", " sec", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", "Number of Measurements:", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", "SMU 2", None))
        self.ds_param_current_2.setText(QCoreApplication.translate("MainWindow", "Current", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", "Sourcemeter:", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", "Compliance:", None))
        self.ds_param_voltage_2.setText(QCoreApplication.translate("MainWindow", "Voltage", None))
        self.ds_smu_select_2.setItemText(0, QCoreApplication.translate("MainWindow", "Simulated", None))

        self.label_71.setText(QCoreApplication.translate("MainWindow", "Mode:", None))
        self.ds_param_compliance_2.setSuffix(QCoreApplication.translate("MainWindow", " A", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", "Output:", None))
        self.ds_param_output_2.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", "Data", None))
        self.ds_file_output.setText(QCoreApplication.translate("MainWindow", "File Output", None))
        self.ds_file_output_path.setText(QCoreApplication.translate("MainWindow", "No data save location specified", None))
        self.ds_save_last_run.setText(QCoreApplication.translate("MainWindow", "Save Last Run", None))
        self.ds_stream.setText(QCoreApplication.translate("MainWindow", "Start Streaming", None))
        self.ds_left_plot_settings.setText(QCoreApplication.translate("MainWindow", "Left Plot Settings", None))
        self.ds_right_plot_settings.setText(QCoreApplication.translate("MainWindow", "Right Plot Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data_stream), QCoreApplication.translate("MainWindow", "Data Streaming", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", "Sweep Measurements", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", "Data Stream Measurements", None))
        self.plot_parameters.setText(QCoreApplication.translate("MainWindow", "Plot Parameters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data_view), QCoreApplication.translate("MainWindow", "Data", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", "Tools", None))

    # retranslateUi
