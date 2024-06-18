# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowjuLDrR.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

from DataPlot import DataPlot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 850)
        MainWindow.setMinimumSize(QSize(900, 850))
        self.menubar_sourcemeter_connections = QAction(MainWindow)
        self.menubar_sourcemeter_connections.setObjectName(u"menubar_sourcemeter_connections")
        self.menubar_save_configuration = QAction(MainWindow)
        self.menubar_save_configuration.setObjectName(u"menubar_save_configuration")
        self.menubar_load_configuration = QAction(MainWindow)
        self.menubar_load_configuration.setObjectName(u"menubar_load_configuration")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_connect = QWidget()
        self.tab_connect.setObjectName(u"tab_connect")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_connect)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.smu_connections = QGroupBox(self.tab_connect)
        self.smu_connections.setObjectName(u"smu_connections")
        self.verticalLayout_7 = QVBoxLayout(self.smu_connections)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.smu_connection_list = QListWidget(self.smu_connections)
        self.smu_connection_list.setObjectName(u"smu_connection_list")

        self.verticalLayout_7.addWidget(self.smu_connection_list)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.smu_disconnect = QPushButton(self.smu_connections)
        self.smu_disconnect.setObjectName(u"smu_disconnect")
        self.smu_disconnect.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.smu_disconnect)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.smu_identify = QPushButton(self.smu_connections)
        self.smu_identify.setObjectName(u"smu_identify")
        self.smu_identify.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.smu_identify)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addWidget(self.smu_connections)

        self.groupBox_4 = QGroupBox(self.tab_connect)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.smu_search_log = QPlainTextEdit(self.groupBox_4)
        self.smu_search_log.setObjectName(u"smu_search_log")
        self.smu_search_log.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.smu_search_log.setReadOnly(True)
        self.smu_search_log.setCenterOnScroll(True)

        self.verticalLayout_8.addWidget(self.smu_search_log)

        self.smu_search_progress = QProgressBar(self.groupBox_4)
        self.smu_search_progress.setObjectName(u"smu_search_progress")

        self.verticalLayout_8.addWidget(self.smu_search_progress)

        self.smu_search = QPushButton(self.groupBox_4)
        self.smu_search.setObjectName(u"smu_search")
        self.smu_search.setEnabled(True)

        self.verticalLayout_8.addWidget(self.smu_search)


        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.tabWidget.addTab(self.tab_connect, "")
        self.tab_sweep_measurement = QWidget()
        self.tab_sweep_measurement.setObjectName(u"tab_sweep_measurement")
        self.gridLayout = QGridLayout(self.tab_sweep_measurement)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(self.tab_sweep_measurement)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(425, 0))
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)

        self.sm_meta_comments = QPlainTextEdit(self.groupBox_3)
        self.sm_meta_comments.setObjectName(u"sm_meta_comments")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sm_meta_comments.sizePolicy().hasHeightForWidth())
        self.sm_meta_comments.setSizePolicy(sizePolicy)
        self.sm_meta_comments.setMaximumSize(QSize(16777215, 80))

        self.gridLayout_3.addWidget(self.sm_meta_comments, 2, 1, 1, 4)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.sm_meta_wafer = QLineEdit(self.groupBox_3)
        self.sm_meta_wafer.setObjectName(u"sm_meta_wafer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sm_meta_wafer.sizePolicy().hasHeightForWidth())
        self.sm_meta_wafer.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.sm_meta_wafer, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 1, 2, 1, 1)

        self.sm_meta_light = QRadioButton(self.groupBox_3)
        self.sm_meta_light.setObjectName(u"sm_meta_light")

        self.gridLayout_3.addWidget(self.sm_meta_light, 1, 4, 1, 1)

        self.sm_meta_dark = QRadioButton(self.groupBox_3)
        self.sm_meta_dark.setObjectName(u"sm_meta_dark")

        self.gridLayout_3.addWidget(self.sm_meta_dark, 1, 3, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)

        self.sm_meta_step = QLineEdit(self.groupBox_3)
        self.sm_meta_step.setObjectName(u"sm_meta_step")
        sizePolicy1.setHeightForWidth(self.sm_meta_step.sizePolicy().hasHeightForWidth())
        self.sm_meta_step.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.sm_meta_step, 1, 1, 1, 1)

        self.sm_meta_chip = QLineEdit(self.groupBox_3)
        self.sm_meta_chip.setObjectName(u"sm_meta_chip")
        sizePolicy1.setHeightForWidth(self.sm_meta_chip.sizePolicy().hasHeightForWidth())
        self.sm_meta_chip.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.sm_meta_chip, 0, 3, 1, 2)


        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.tab_sweep_measurement)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(425, 0))
        self.gridLayout_9 = QGridLayout(self.groupBox_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.sm_abort = QPushButton(self.groupBox_8)
        self.sm_abort.setObjectName(u"sm_abort")
        self.sm_abort.setEnabled(False)

        self.gridLayout_9.addWidget(self.sm_abort, 1, 1, 1, 1)

        self.sm_file_output = QPushButton(self.groupBox_8)
        self.sm_file_output.setObjectName(u"sm_file_output")

        self.gridLayout_9.addWidget(self.sm_file_output, 0, 0, 1, 1)

        self.sm_save_last_run = QPushButton(self.groupBox_8)
        self.sm_save_last_run.setObjectName(u"sm_save_last_run")
        self.sm_save_last_run.setEnabled(False)

        self.gridLayout_9.addWidget(self.sm_save_last_run, 1, 0, 1, 1)

        self.sm_left_plot_settings = QPushButton(self.groupBox_8)
        self.sm_left_plot_settings.setObjectName(u"sm_left_plot_settings")

        self.gridLayout_9.addWidget(self.sm_left_plot_settings, 2, 0, 1, 1)

        self.sm_progress = QProgressBar(self.groupBox_8)
        self.sm_progress.setObjectName(u"sm_progress")
        self.sm_progress.setValue(0)
        self.sm_progress.setTextVisible(False)

        self.gridLayout_9.addWidget(self.sm_progress, 3, 0, 1, 2)

        self.sm_file_output_path = QLabel(self.groupBox_8)
        self.sm_file_output_path.setObjectName(u"sm_file_output_path")

        self.gridLayout_9.addWidget(self.sm_file_output_path, 0, 1, 1, 1)

        self.sm_right_plot_settings = QPushButton(self.groupBox_8)
        self.sm_right_plot_settings.setObjectName(u"sm_right_plot_settings")

        self.gridLayout_9.addWidget(self.sm_right_plot_settings, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_8, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab_sweep_measurement)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(425, 0))
        self.gridLayout_11 = QGridLayout(self.groupBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label_4, 2, 2, 1, 1)

        self.sm_param_sweep_end = QDoubleSpinBox(self.groupBox)
        self.sm_param_sweep_end.setObjectName(u"sm_param_sweep_end")
        self.sm_param_sweep_end.setDecimals(6)
        self.sm_param_sweep_end.setMinimum(-1000.000000000000000)
        self.sm_param_sweep_end.setMaximum(1000.000000000000000)
        self.sm_param_sweep_end.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_11.addWidget(self.sm_param_sweep_end, 3, 2, 1, 1)

        self.sm_param_sweep_start = QDoubleSpinBox(self.groupBox)
        self.sm_param_sweep_start.setObjectName(u"sm_param_sweep_start")
        self.sm_param_sweep_start.setDecimals(6)
        self.sm_param_sweep_start.setMinimum(-1000.000000000000000)
        self.sm_param_sweep_start.setMaximum(1000.000000000000000)
        self.sm_param_sweep_start.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_11.addWidget(self.sm_param_sweep_start, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label, 2, 0, 1, 1)

        self.sm_param_sweep_step = QDoubleSpinBox(self.groupBox)
        self.sm_param_sweep_step.setObjectName(u"sm_param_sweep_step")
        self.sm_param_sweep_step.setDecimals(6)
        self.sm_param_sweep_step.setMinimum(-1000.000000000000000)
        self.sm_param_sweep_step.setMaximum(1000.000000000000000)
        self.sm_param_sweep_step.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_11.addWidget(self.sm_param_sweep_step, 3, 1, 1, 1)

        self.sm_param_sweep_voltage = QRadioButton(self.groupBox)
        self.sm_param_sweep_voltage.setObjectName(u"sm_param_sweep_voltage")
        self.sm_param_sweep_voltage.setChecked(True)

        self.gridLayout_11.addWidget(self.sm_param_sweep_voltage, 1, 1, 1, 1)

        self.sm_param_sweep_current = QRadioButton(self.groupBox)
        self.sm_param_sweep_current.setObjectName(u"sm_param_sweep_current")

        self.gridLayout_11.addWidget(self.sm_param_sweep_current, 1, 2, 1, 1)

        self.sm_sweep_smu = QComboBox(self.groupBox)
        self.sm_sweep_smu.addItem("")
        self.sm_sweep_smu.setObjectName(u"sm_sweep_smu")

        self.gridLayout_11.addWidget(self.sm_sweep_smu, 0, 1, 1, 2)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_11.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_11.addWidget(self.label_17, 4, 0, 1, 1)

        self.sm_param_sweep_compliance = QDoubleSpinBox(self.groupBox)
        self.sm_param_sweep_compliance.setObjectName(u"sm_param_sweep_compliance")
        self.sm_param_sweep_compliance.setDecimals(6)
        self.sm_param_sweep_compliance.setMaximum(1000.000000000000000)
        self.sm_param_sweep_compliance.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_param_sweep_compliance.setValue(0.000000000000000)

        self.gridLayout_11.addWidget(self.sm_param_sweep_compliance, 4, 1, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_sweep_measurement)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(425, 0))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sm_param_constant_current = QRadioButton(self.groupBox_2)
        self.sm_param_constant_current.setObjectName(u"sm_param_constant_current")

        self.gridLayout_2.addWidget(self.sm_param_constant_current, 1, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)

        self.sm_param_constant_voltage = QRadioButton(self.groupBox_2)
        self.sm_param_constant_voltage.setObjectName(u"sm_param_constant_voltage")
        self.sm_param_constant_voltage.setChecked(True)

        self.gridLayout_2.addWidget(self.sm_param_constant_voltage, 1, 1, 1, 1)

        self.sm_constant_smu = QComboBox(self.groupBox_2)
        self.sm_constant_smu.addItem("")
        self.sm_constant_smu.setObjectName(u"sm_constant_smu")

        self.gridLayout_2.addWidget(self.sm_constant_smu, 0, 1, 1, 2)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.sm_param_constant_compliance = QDoubleSpinBox(self.groupBox_2)
        self.sm_param_constant_compliance.setObjectName(u"sm_param_constant_compliance")
        self.sm_param_constant_compliance.setDecimals(6)
        self.sm_param_constant_compliance.setMaximum(1000.000000000000000)
        self.sm_param_constant_compliance.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_param_constant_compliance.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.sm_param_constant_compliance, 3, 1, 1, 2)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)

        self.sm_param_constant_output = QDoubleSpinBox(self.groupBox_2)
        self.sm_param_constant_output.setObjectName(u"sm_param_constant_output")
        self.sm_param_constant_output.setDecimals(6)
        self.sm_param_constant_output.setMinimum(-1000.000000000000000)
        self.sm_param_constant_output.setMaximum(1000.000000000000000)
        self.sm_param_constant_output.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_2.addWidget(self.sm_param_constant_output, 2, 1, 1, 2)


        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.tab_sweep_measurement)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(425, 0))
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.sm_param_quick_sweep_step_override = QDoubleSpinBox(self.groupBox_7)
        self.sm_param_quick_sweep_step_override.setObjectName(u"sm_param_quick_sweep_step_override")
        self.sm_param_quick_sweep_step_override.setDecimals(6)
        self.sm_param_quick_sweep_step_override.setMaximum(1000.000000000000000)
        self.sm_param_quick_sweep_step_override.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_10.addWidget(self.sm_param_quick_sweep_step_override, 1, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_28, 1, 0, 1, 1)

        self.sm_run_quick_measurement = QPushButton(self.groupBox_7)
        self.sm_run_quick_measurement.setObjectName(u"sm_run_quick_measurement")

        self.gridLayout_10.addWidget(self.sm_run_quick_measurement, 2, 0, 1, 2)

        self.sm_param_quick_pause_between_measurements = QDoubleSpinBox(self.groupBox_7)
        self.sm_param_quick_pause_between_measurements.setObjectName(u"sm_param_quick_pause_between_measurements")
        self.sm_param_quick_pause_between_measurements.setDecimals(3)
        self.sm_param_quick_pause_between_measurements.setMaximum(100.000000000000000)
        self.sm_param_quick_pause_between_measurements.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_10.addWidget(self.sm_param_quick_pause_between_measurements, 0, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_7)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_10.addWidget(self.label_29, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_7, 2, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_sweep_measurement)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(425, 0))
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.sm_run_full_measurement = QPushButton(self.groupBox_6)
        self.sm_run_full_measurement.setObjectName(u"sm_run_full_measurement")

        self.gridLayout_6.addWidget(self.sm_run_full_measurement, 3, 0, 1, 2)

        self.label_22 = QLabel(self.groupBox_6)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_6.addWidget(self.label_22, 0, 0, 1, 1)

        self.sm_param_pause_between_measurements = QDoubleSpinBox(self.groupBox_6)
        self.sm_param_pause_between_measurements.setObjectName(u"sm_param_pause_between_measurements")
        self.sm_param_pause_between_measurements.setDecimals(3)
        self.sm_param_pause_between_measurements.setMaximum(100.000000000000000)
        self.sm_param_pause_between_measurements.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_6.addWidget(self.sm_param_pause_between_measurements, 1, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_6)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_6.addWidget(self.label_25, 2, 0, 1, 1)

        self.sm_param_number_of_sweeps = QSpinBox(self.groupBox_6)
        self.sm_param_number_of_sweeps.setObjectName(u"sm_param_number_of_sweeps")
        self.sm_param_number_of_sweeps.setMaximum(100)
        self.sm_param_number_of_sweeps.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_param_number_of_sweeps.setValue(1)

        self.gridLayout_6.addWidget(self.sm_param_number_of_sweeps, 0, 1, 1, 1)

        self.sm_param_pause_between_sweeps = QDoubleSpinBox(self.groupBox_6)
        self.sm_param_pause_between_sweeps.setObjectName(u"sm_param_pause_between_sweeps")
        self.sm_param_pause_between_sweeps.setDecimals(3)
        self.sm_param_pause_between_sweeps.setMaximum(100.000000000000000)
        self.sm_param_pause_between_sweeps.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_6.addWidget(self.sm_param_pause_between_sweeps, 2, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_6)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_6.addWidget(self.label_26, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_6, 2, 1, 1, 1)

        self.sm_plot_1 = DataPlot(self.tab_sweep_measurement)
        self.sm_plot_1.setObjectName(u"sm_plot_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.sm_plot_1.sizePolicy().hasHeightForWidth())
        self.sm_plot_1.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.sm_plot_1, 3, 0, 1, 1)

        self.sm_plot_2 = DataPlot(self.tab_sweep_measurement)
        self.sm_plot_2.setObjectName(u"sm_plot_2")
        sizePolicy3.setHeightForWidth(self.sm_plot_2.sizePolicy().hasHeightForWidth())
        self.sm_plot_2.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.sm_plot_2, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tab_sweep_measurement, "")
        self.tab_data_stream = QWidget()
        self.tab_data_stream.setObjectName(u"tab_data_stream")
        self.gridLayout_12 = QGridLayout(self.tab_data_stream)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_5 = QGroupBox(self.tab_data_stream)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(425, 0))
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_30 = QLabel(self.groupBox_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 1, 0, 1, 1)

        self.ds_meta_comments = QPlainTextEdit(self.groupBox_5)
        self.ds_meta_comments.setObjectName(u"ds_meta_comments")
        sizePolicy.setHeightForWidth(self.ds_meta_comments.sizePolicy().hasHeightForWidth())
        self.ds_meta_comments.setSizePolicy(sizePolicy)
        self.ds_meta_comments.setMaximumSize(QSize(16777215, 80))

        self.gridLayout_5.addWidget(self.ds_meta_comments, 2, 1, 1, 4)

        self.label_31 = QLabel(self.groupBox_5)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 0, 0, 1, 1)

        self.ds_meta_wafer = QLineEdit(self.groupBox_5)
        self.ds_meta_wafer.setObjectName(u"ds_meta_wafer")
        sizePolicy1.setHeightForWidth(self.ds_meta_wafer.sizePolicy().hasHeightForWidth())
        self.ds_meta_wafer.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.ds_meta_wafer, 0, 1, 1, 1)

        self.label_32 = QLabel(self.groupBox_5)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 1, 2, 1, 1)

        self.ds_meta_light = QRadioButton(self.groupBox_5)
        self.ds_meta_light.setObjectName(u"ds_meta_light")

        self.gridLayout_5.addWidget(self.ds_meta_light, 1, 4, 1, 1)

        self.ds_meta_dark = QRadioButton(self.groupBox_5)
        self.ds_meta_dark.setObjectName(u"ds_meta_dark")

        self.gridLayout_5.addWidget(self.ds_meta_dark, 1, 3, 1, 1)

        self.label_33 = QLabel(self.groupBox_5)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_5.addWidget(self.label_33, 0, 2, 1, 1)

        self.label_34 = QLabel(self.groupBox_5)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_5.addWidget(self.label_34, 2, 0, 1, 1)

        self.ds_meta_step = QLineEdit(self.groupBox_5)
        self.ds_meta_step.setObjectName(u"ds_meta_step")
        sizePolicy1.setHeightForWidth(self.ds_meta_step.sizePolicy().hasHeightForWidth())
        self.ds_meta_step.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.ds_meta_step, 1, 1, 1, 1)

        self.ds_meta_chip = QLineEdit(self.groupBox_5)
        self.ds_meta_chip.setObjectName(u"ds_meta_chip")
        sizePolicy1.setHeightForWidth(self.ds_meta_chip.sizePolicy().hasHeightForWidth())
        self.ds_meta_chip.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.ds_meta_chip, 0, 3, 1, 2)


        self.gridLayout_12.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.tab_data_stream)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setMinimumSize(QSize(425, 0))
        self.gridLayout_19 = QGridLayout(self.groupBox_15)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.ds_param_current_1 = QRadioButton(self.groupBox_15)
        self.ds_param_current_1.setObjectName(u"ds_param_current_1")

        self.gridLayout_19.addWidget(self.ds_param_current_1, 1, 2, 1, 1)

        self.label_53 = QLabel(self.groupBox_15)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_19.addWidget(self.label_53, 0, 0, 1, 1)

        self.label_54 = QLabel(self.groupBox_15)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_19.addWidget(self.label_54, 3, 0, 1, 1)

        self.ds_param_voltage_1 = QRadioButton(self.groupBox_15)
        self.ds_param_voltage_1.setObjectName(u"ds_param_voltage_1")
        self.ds_param_voltage_1.setChecked(True)

        self.gridLayout_19.addWidget(self.ds_param_voltage_1, 1, 1, 1, 1)

        self.ds_smu_1 = QComboBox(self.groupBox_15)
        self.ds_smu_1.addItem("")
        self.ds_smu_1.setObjectName(u"ds_smu_1")

        self.gridLayout_19.addWidget(self.ds_smu_1, 0, 1, 1, 2)

        self.label_55 = QLabel(self.groupBox_15)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_19.addWidget(self.label_55, 1, 0, 1, 1)

        self.ds_param_compliance_1 = QDoubleSpinBox(self.groupBox_15)
        self.ds_param_compliance_1.setObjectName(u"ds_param_compliance_1")
        self.ds_param_compliance_1.setDecimals(6)
        self.ds_param_compliance_1.setMinimum(0.000000000000000)
        self.ds_param_compliance_1.setMaximum(1000.000000000000000)
        self.ds_param_compliance_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_19.addWidget(self.ds_param_compliance_1, 3, 1, 1, 2)

        self.label_56 = QLabel(self.groupBox_15)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_19.addWidget(self.label_56, 2, 0, 1, 1)

        self.ds_param_output_1 = QDoubleSpinBox(self.groupBox_15)
        self.ds_param_output_1.setObjectName(u"ds_param_output_1")
        self.ds_param_output_1.setDecimals(6)
        self.ds_param_output_1.setMinimum(-1000.000000000000000)
        self.ds_param_output_1.setMaximum(1000.000000000000000)
        self.ds_param_output_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_19.addWidget(self.ds_param_output_1, 2, 1, 1, 2)


        self.gridLayout_12.addWidget(self.groupBox_15, 3, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.tab_data_stream)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_24 = QGridLayout(self.groupBox_20)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.ds_param_fixed_duration = QRadioButton(self.groupBox_20)
        self.ds_param_fixed_duration.setObjectName(u"ds_param_fixed_duration")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ds_param_fixed_duration.sizePolicy().hasHeightForWidth())
        self.ds_param_fixed_duration.setSizePolicy(sizePolicy4)

        self.gridLayout_24.addWidget(self.ds_param_fixed_duration, 2, 0, 1, 1)

        self.label_73 = QLabel(self.groupBox_20)
        self.label_73.setObjectName(u"label_73")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy5)

        self.gridLayout_24.addWidget(self.label_73, 0, 2, 1, 1)

        self.ds_param_fixed_number = QRadioButton(self.groupBox_20)
        self.ds_param_fixed_number.setObjectName(u"ds_param_fixed_number")
        sizePolicy4.setHeightForWidth(self.ds_param_fixed_number.sizePolicy().hasHeightForWidth())
        self.ds_param_fixed_number.setSizePolicy(sizePolicy4)

        self.gridLayout_24.addWidget(self.ds_param_fixed_number, 1, 0, 1, 1)

        self.ds_param_duration = QDoubleSpinBox(self.groupBox_20)
        self.ds_param_duration.setObjectName(u"ds_param_duration")
        self.ds_param_duration.setEnabled(False)
        self.ds_param_duration.setDecimals(3)
        self.ds_param_duration.setMaximum(100.000000000000000)
        self.ds_param_duration.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_24.addWidget(self.ds_param_duration, 0, 3, 1, 1)

        self.ds_param_continuous = QRadioButton(self.groupBox_20)
        self.ds_param_continuous.setObjectName(u"ds_param_continuous")
        sizePolicy4.setHeightForWidth(self.ds_param_continuous.sizePolicy().hasHeightForWidth())
        self.ds_param_continuous.setSizePolicy(sizePolicy4)
        self.ds_param_continuous.setChecked(True)

        self.gridLayout_24.addWidget(self.ds_param_continuous, 0, 0, 1, 1)

        self.line_3 = QFrame(self.groupBox_20)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_24.addWidget(self.line_3, 0, 1, 3, 1)

        self.label_74 = QLabel(self.groupBox_20)
        self.label_74.setObjectName(u"label_74")
        sizePolicy5.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy5)

        self.gridLayout_24.addWidget(self.label_74, 2, 2, 1, 1)

        self.ds_param_pause_between_measurements = QDoubleSpinBox(self.groupBox_20)
        self.ds_param_pause_between_measurements.setObjectName(u"ds_param_pause_between_measurements")
        self.ds_param_pause_between_measurements.setDecimals(3)
        self.ds_param_pause_between_measurements.setMaximum(100.000000000000000)
        self.ds_param_pause_between_measurements.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_24.addWidget(self.ds_param_pause_between_measurements, 2, 3, 1, 1)

        self.label_75 = QLabel(self.groupBox_20)
        self.label_75.setObjectName(u"label_75")
        sizePolicy5.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy5)

        self.gridLayout_24.addWidget(self.label_75, 1, 2, 1, 1)

        self.ds_param_number_of_measurements = QSpinBox(self.groupBox_20)
        self.ds_param_number_of_measurements.setObjectName(u"ds_param_number_of_measurements")
        self.ds_param_number_of_measurements.setEnabled(False)
        self.ds_param_number_of_measurements.setMaximum(100)
        self.ds_param_number_of_measurements.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_24.addWidget(self.ds_param_number_of_measurements, 1, 3, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_20, 2, 0, 1, 1)

        self.groupBox_19 = QGroupBox(self.tab_data_stream)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setMinimumSize(QSize(425, 0))
        self.gridLayout_23 = QGridLayout(self.groupBox_19)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.ds_param_current_2 = QRadioButton(self.groupBox_19)
        self.ds_param_current_2.setObjectName(u"ds_param_current_2")

        self.gridLayout_23.addWidget(self.ds_param_current_2, 1, 2, 1, 1)

        self.label_69 = QLabel(self.groupBox_19)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_23.addWidget(self.label_69, 0, 0, 1, 1)

        self.label_70 = QLabel(self.groupBox_19)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_23.addWidget(self.label_70, 3, 0, 1, 1)

        self.ds_param_voltage_2 = QRadioButton(self.groupBox_19)
        self.ds_param_voltage_2.setObjectName(u"ds_param_voltage_2")
        self.ds_param_voltage_2.setChecked(True)

        self.gridLayout_23.addWidget(self.ds_param_voltage_2, 1, 1, 1, 1)

        self.ds_smu_2 = QComboBox(self.groupBox_19)
        self.ds_smu_2.addItem("")
        self.ds_smu_2.setObjectName(u"ds_smu_2")

        self.gridLayout_23.addWidget(self.ds_smu_2, 0, 1, 1, 2)

        self.label_71 = QLabel(self.groupBox_19)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_23.addWidget(self.label_71, 1, 0, 1, 1)

        self.ds_param_compliance_2 = QDoubleSpinBox(self.groupBox_19)
        self.ds_param_compliance_2.setObjectName(u"ds_param_compliance_2")
        self.ds_param_compliance_2.setDecimals(6)
        self.ds_param_compliance_2.setMinimum(0.000000000000000)
        self.ds_param_compliance_2.setMaximum(1000.000000000000000)
        self.ds_param_compliance_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_23.addWidget(self.ds_param_compliance_2, 3, 1, 1, 2)

        self.label_72 = QLabel(self.groupBox_19)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_23.addWidget(self.label_72, 2, 0, 1, 1)

        self.ds_param_output_2 = QDoubleSpinBox(self.groupBox_19)
        self.ds_param_output_2.setObjectName(u"ds_param_output_2")
        self.ds_param_output_2.setDecimals(6)
        self.ds_param_output_2.setMinimum(-1000.000000000000000)
        self.ds_param_output_2.setMaximum(1000.000000000000000)
        self.ds_param_output_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_23.addWidget(self.ds_param_output_2, 2, 1, 1, 2)


        self.gridLayout_12.addWidget(self.groupBox_19, 3, 1, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_data_stream)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(425, 0))
        self.gridLayout_18 = QGridLayout(self.groupBox_14)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.ds_file_output = QPushButton(self.groupBox_14)
        self.ds_file_output.setObjectName(u"ds_file_output")

        self.gridLayout_18.addWidget(self.ds_file_output, 0, 0, 1, 1)

        self.ds_progress = QProgressBar(self.groupBox_14)
        self.ds_progress.setObjectName(u"ds_progress")
        self.ds_progress.setValue(0)
        self.ds_progress.setTextVisible(False)

        self.gridLayout_18.addWidget(self.ds_progress, 3, 0, 1, 2)

        self.ds_file_output_path = QLabel(self.groupBox_14)
        self.ds_file_output_path.setObjectName(u"ds_file_output_path")

        self.gridLayout_18.addWidget(self.ds_file_output_path, 0, 1, 1, 1)

        self.ds_save_last_run = QPushButton(self.groupBox_14)
        self.ds_save_last_run.setObjectName(u"ds_save_last_run")
        self.ds_save_last_run.setEnabled(False)

        self.gridLayout_18.addWidget(self.ds_save_last_run, 1, 0, 1, 1)

        self.ds_stream = QPushButton(self.groupBox_14)
        self.ds_stream.setObjectName(u"ds_stream")
        self.ds_stream.setEnabled(True)

        self.gridLayout_18.addWidget(self.ds_stream, 1, 1, 1, 1)

        self.ds_left_plot_settings = QPushButton(self.groupBox_14)
        self.ds_left_plot_settings.setObjectName(u"ds_left_plot_settings")

        self.gridLayout_18.addWidget(self.ds_left_plot_settings, 2, 0, 1, 1)

        self.ds_right_plot_settings = QPushButton(self.groupBox_14)
        self.ds_right_plot_settings.setObjectName(u"ds_right_plot_settings")

        self.gridLayout_18.addWidget(self.ds_right_plot_settings, 2, 1, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_14, 0, 1, 1, 1)

        self.ds_plot_1 = DataPlot(self.tab_data_stream)
        self.ds_plot_1.setObjectName(u"ds_plot_1")
        sizePolicy3.setHeightForWidth(self.ds_plot_1.sizePolicy().hasHeightForWidth())
        self.ds_plot_1.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ds_plot_1, 5, 0, 1, 1)

        self.ds_plot_2 = DataPlot(self.tab_data_stream)
        self.ds_plot_2.setObjectName(u"ds_plot_2")
        sizePolicy3.setHeightForWidth(self.ds_plot_2.sizePolicy().hasHeightForWidth())
        self.ds_plot_2.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ds_plot_2, 5, 1, 1, 1)

        self.tabWidget.addTab(self.tab_data_stream, "")
        self.tab_data = QWidget()
        self.tab_data.setObjectName(u"tab_data")
        self.gridLayout_7 = QGridLayout(self.tab_data)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.data_plot = DataPlot(self.tab_data)
        self.data_plot.setObjectName(u"data_plot")

        self.gridLayout_7.addWidget(self.data_plot, 0, 0, 1, 2)

        self.groupBox_9 = QGroupBox(self.tab_data)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy2.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.groupBox_9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sweep_measurements = QListWidget(self.groupBox_9)
        self.sweep_measurements.setObjectName(u"sweep_measurements")
        self.sweep_measurements.setMaximumSize(QSize(16777215, 200))
        self.sweep_measurements.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.sweep_measurements)


        self.gridLayout_7.addWidget(self.groupBox_9, 2, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.tab_data)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy2.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.datastream_measurements = QListWidget(self.groupBox_10)
        self.datastream_measurements.setObjectName(u"datastream_measurements")
        self.datastream_measurements.setMaximumSize(QSize(16777215, 200))
        self.datastream_measurements.setAlternatingRowColors(True)

        self.verticalLayout_2.addWidget(self.datastream_measurements)


        self.gridLayout_7.addWidget(self.groupBox_10, 2, 1, 1, 1)

        self.plot_parameters = QPushButton(self.tab_data)
        self.plot_parameters.setObjectName(u"plot_parameters")

        self.gridLayout_7.addWidget(self.plot_parameters, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_data, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 900, 22))
        self.menuTools = QMenu(self.menuBar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.sm_meta_wafer, self.sm_meta_chip)
        QWidget.setTabOrder(self.sm_meta_chip, self.sm_meta_step)
        QWidget.setTabOrder(self.sm_meta_step, self.sm_meta_dark)
        QWidget.setTabOrder(self.sm_meta_dark, self.sm_meta_light)
        QWidget.setTabOrder(self.sm_meta_light, self.sm_meta_comments)
        QWidget.setTabOrder(self.sm_meta_comments, self.sm_sweep_smu)
        QWidget.setTabOrder(self.sm_sweep_smu, self.sm_param_sweep_voltage)
        QWidget.setTabOrder(self.sm_param_sweep_voltage, self.sm_param_sweep_current)
        QWidget.setTabOrder(self.sm_param_sweep_current, self.sm_param_sweep_start)
        QWidget.setTabOrder(self.sm_param_sweep_start, self.sm_param_sweep_step)
        QWidget.setTabOrder(self.sm_param_sweep_step, self.sm_param_sweep_end)
        QWidget.setTabOrder(self.sm_param_sweep_end, self.sm_param_sweep_compliance)
        QWidget.setTabOrder(self.sm_param_sweep_compliance, self.sm_constant_smu)
        QWidget.setTabOrder(self.sm_constant_smu, self.sm_param_constant_voltage)
        QWidget.setTabOrder(self.sm_param_constant_voltage, self.sm_param_constant_current)
        QWidget.setTabOrder(self.sm_param_constant_current, self.sm_param_constant_output)
        QWidget.setTabOrder(self.sm_param_constant_output, self.sm_param_constant_compliance)
        QWidget.setTabOrder(self.sm_param_constant_compliance, self.sm_param_quick_pause_between_measurements)
        QWidget.setTabOrder(self.sm_param_quick_pause_between_measurements, self.sm_param_quick_sweep_step_override)
        QWidget.setTabOrder(self.sm_param_quick_sweep_step_override, self.sm_param_number_of_sweeps)
        QWidget.setTabOrder(self.sm_param_number_of_sweeps, self.sm_param_pause_between_measurements)
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
        QWidget.setTabOrder(self.ds_param_pause_between_measurements, self.ds_smu_1)
        QWidget.setTabOrder(self.ds_smu_1, self.ds_param_voltage_1)
        QWidget.setTabOrder(self.ds_param_voltage_1, self.ds_param_current_1)
        QWidget.setTabOrder(self.ds_param_current_1, self.ds_param_output_1)
        QWidget.setTabOrder(self.ds_param_output_1, self.ds_param_compliance_1)
        QWidget.setTabOrder(self.ds_param_compliance_1, self.ds_smu_2)
        QWidget.setTabOrder(self.ds_smu_2, self.ds_param_voltage_2)
        QWidget.setTabOrder(self.ds_param_voltage_2, self.ds_param_current_2)
        QWidget.setTabOrder(self.ds_param_current_2, self.ds_param_output_2)
        QWidget.setTabOrder(self.ds_param_output_2, self.ds_param_compliance_2)
        QWidget.setTabOrder(self.ds_param_compliance_2, self.ds_file_output)
        QWidget.setTabOrder(self.ds_file_output, self.ds_save_last_run)
        QWidget.setTabOrder(self.ds_save_last_run, self.ds_stream)
        QWidget.setTabOrder(self.ds_stream, self.ds_left_plot_settings)
        QWidget.setTabOrder(self.ds_left_plot_settings, self.ds_right_plot_settings)
        QWidget.setTabOrder(self.ds_right_plot_settings, self.smu_identify)
        QWidget.setTabOrder(self.smu_identify, self.smu_connection_list)
        QWidget.setTabOrder(self.smu_connection_list, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.smu_disconnect)
        QWidget.setTabOrder(self.smu_disconnect, self.smu_search)
        QWidget.setTabOrder(self.smu_search, self.smu_search_log)

        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuTools.addAction(self.menubar_sourcemeter_connections)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.menubar_save_configuration)
        self.menuTools.addAction(self.menubar_load_configuration)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dual SMU Controller", None))
        self.menubar_sourcemeter_connections.setText(QCoreApplication.translate("MainWindow", u"Sourcemeter Connections", None))
        self.menubar_save_configuration.setText(QCoreApplication.translate("MainWindow", u"Save Configuration", None))
        self.menubar_load_configuration.setText(QCoreApplication.translate("MainWindow", u"Load Configuration", None))
        self.smu_connections.setTitle(QCoreApplication.translate("MainWindow", u"Connections", None))
        self.smu_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.smu_identify.setText(QCoreApplication.translate("MainWindow", u"Identify", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Connect to Sourcemeters", None))
        self.smu_search.setText(QCoreApplication.translate("MainWindow", u"Search for SMUs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_connect), QCoreApplication.translate("MainWindow", u"Sourcemeter Connections", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Step of Process:", None))
        self.sm_meta_comments.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter comments here...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Waver #:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Light:", None))
        self.sm_meta_light.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.sm_meta_dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Chip #:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Comments:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.sm_abort.setText(QCoreApplication.translate("MainWindow", u"Abort Measurement", None))
        self.sm_file_output.setText(QCoreApplication.translate("MainWindow", u"File Output", None))
        self.sm_save_last_run.setText(QCoreApplication.translate("MainWindow", u"Save Last Run", None))
        self.sm_left_plot_settings.setText(QCoreApplication.translate("MainWindow", u"Left Plot Settings", None))
        self.sm_file_output_path.setText(QCoreApplication.translate("MainWindow", u"No data save location specified", None))
        self.sm_right_plot_settings.setText(QCoreApplication.translate("MainWindow", u"Left Plot Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sweep Parameters", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.sm_param_sweep_end.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.sm_param_sweep_start.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.sm_param_sweep_step.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.sm_param_sweep_voltage.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.sm_param_sweep_current.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.sm_sweep_smu.setItemText(0, QCoreApplication.translate("MainWindow", u"Simulated", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sourcemeter (smu_1):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Compliance:", None))
        self.sm_param_sweep_compliance.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Constant Parameters", None))
        self.sm_param_constant_current.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sourcemeter (smu_2):", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Compliance:", None))
        self.sm_param_constant_voltage.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.sm_constant_smu.setItemText(0, QCoreApplication.translate("MainWindow", u"Simulated", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.sm_param_constant_compliance.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.sm_param_constant_output.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Quick Measurement", None))
        self.sm_param_quick_sweep_step_override.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Sweep Step Override:", None))
        self.sm_run_quick_measurement.setText(QCoreApplication.translate("MainWindow", u"Run Quick Measurement", None))
        self.sm_param_quick_pause_between_measurements.setSuffix(QCoreApplication.translate("MainWindow", u" sec", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Pause Between Measurements:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Full Measurement", None))
        self.sm_run_full_measurement.setText(QCoreApplication.translate("MainWindow", u"Run Full Measurement", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Number of Sweeps:", None))
        self.sm_param_pause_between_measurements.setSuffix(QCoreApplication.translate("MainWindow", u" sec", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Pause Between Sweeps:", None))
        self.sm_param_pause_between_sweeps.setSuffix(QCoreApplication.translate("MainWindow", u" sec", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Pause Between Measurements:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sweep_measurement), QCoreApplication.translate("MainWindow", u"Sweep Measurement", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Step of Process:", None))
        self.ds_meta_comments.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter comments here...", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Waver #:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Light:", None))
        self.ds_meta_light.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.ds_meta_dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Chip #:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Comments:", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"SMU 1", None))
        self.ds_param_current_1.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Sourcemeter:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Compliance:", None))
        self.ds_param_voltage_1.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.ds_smu_1.setItemText(0, QCoreApplication.translate("MainWindow", u"Simulated", None))

        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.ds_param_compliance_1.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.ds_param_output_1.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Streaming Mode", None))
        self.ds_param_fixed_duration.setText(QCoreApplication.translate("MainWindow", u"Fixed Duration", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.ds_param_fixed_number.setText(QCoreApplication.translate("MainWindow", u"Fixed Number", None))
        self.ds_param_duration.setSuffix(QCoreApplication.translate("MainWindow", u" sec", None))
        self.ds_param_continuous.setText(QCoreApplication.translate("MainWindow", u"Continuous", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Pause Between Measurements:", None))
        self.ds_param_pause_between_measurements.setSuffix(QCoreApplication.translate("MainWindow", u" sec", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Number of Measurements:", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"SMU 2", None))
        self.ds_param_current_2.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Sourcemeter:", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Compliance:", None))
        self.ds_param_voltage_2.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.ds_smu_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Simulated", None))

        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.ds_param_compliance_2.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.ds_param_output_2.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.ds_file_output.setText(QCoreApplication.translate("MainWindow", u"File Output", None))
        self.ds_file_output_path.setText(QCoreApplication.translate("MainWindow", u"No data save location specified", None))
        self.ds_save_last_run.setText(QCoreApplication.translate("MainWindow", u"Save Last Run", None))
        self.ds_stream.setText(QCoreApplication.translate("MainWindow", u"Start Streaming", None))
        self.ds_left_plot_settings.setText(QCoreApplication.translate("MainWindow", u"Left Plot Settings", None))
        self.ds_right_plot_settings.setText(QCoreApplication.translate("MainWindow", u"Right Plot Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data_stream), QCoreApplication.translate("MainWindow", u"Data Streaming", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Sweep Measurements", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Data Stream Measurements", None))
        self.plot_parameters.setText(QCoreApplication.translate("MainWindow", u"Plot Parameters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data), QCoreApplication.translate("MainWindow", u"Data", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

