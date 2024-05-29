# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowbKKbJR.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, Qt, QTime, QUrl
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform,)
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox, QFrame, QGridLayout, QGroupBox, QHBoxLayout,
                               QLabel, QLineEdit, QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
                               QSizePolicy, QSpacerItem, QSpinBox, QTabWidget, QTextEdit, QVBoxLayout, QWidget,)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 826)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_connect = QWidget()
        self.tab_connect.setObjectName("tab_connect")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_connect)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.smu_connections = QGroupBox(self.tab_connect)
        self.smu_connections.setObjectName("smu_connections")
        self.verticalLayout_7 = QVBoxLayout(self.smu_connections)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.smu_connection_list = QListWidget(self.smu_connections)
        self.smu_connection_list.setObjectName("smu_connection_list")

        self.verticalLayout_7.addWidget(self.smu_connection_list)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.smu_disconnect = QPushButton(self.smu_connections)
        self.smu_disconnect.setObjectName("smu_disconnect")
        self.smu_disconnect.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.smu_disconnect)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.smu_identify = QPushButton(self.smu_connections)
        self.smu_identify.setObjectName("smu_identify")
        self.smu_identify.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.smu_identify)

        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4.addWidget(self.smu_connections)

        self.groupBox_4 = QGroupBox(self.tab_connect)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.smu_search_log = QPlainTextEdit(self.groupBox_4)
        self.smu_search_log.setObjectName("smu_search_log")
        self.smu_search_log.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.smu_search_log.setReadOnly(True)
        self.smu_search_log.setCenterOnScroll(True)

        self.verticalLayout_8.addWidget(self.smu_search_log)

        self.smu_search_progress = QProgressBar(self.groupBox_4)
        self.smu_search_progress.setObjectName("smu_search_progress")

        self.verticalLayout_8.addWidget(self.smu_search_progress)

        self.smu_search = QPushButton(self.groupBox_4)
        self.smu_search.setObjectName("smu_search")
        self.smu_search.setEnabled(True)

        self.verticalLayout_8.addWidget(self.smu_search)

        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.tabWidget.addTab(self.tab_connect, "")
        self.tab_sweep = QWidget()
        self.tab_sweep.setObjectName("tab_sweep")
        self.verticalLayout = QVBoxLayout(self.tab_sweep)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sm_metadata = QGroupBox(self.tab_sweep)
        self.sm_metadata.setObjectName("sm_metadata")
        self.verticalLayout_20 = QVBoxLayout(self.sm_metadata)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_33 = QLabel(self.sm_metadata)
        self.label_33.setObjectName("label_33")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_33, 2, 0, 1, 1)

        self.sm_chip_num = QLineEdit(self.sm_metadata)
        self.sm_chip_num.setObjectName("sm_chip_num")

        self.gridLayout_10.addWidget(self.sm_chip_num, 0, 3, 1, 1)

        self.label_37 = QLabel(self.sm_metadata)
        self.label_37.setObjectName("label_37")

        self.gridLayout_10.addWidget(self.label_37, 2, 2, 1, 1)

        self.sm_step_of_process = QLineEdit(self.sm_metadata)
        self.sm_step_of_process.setObjectName("sm_step_of_process")

        self.gridLayout_10.addWidget(self.sm_step_of_process, 2, 1, 1, 1)

        self.label_35 = QLabel(self.sm_metadata)
        self.label_35.setObjectName("label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_35, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.sm_metadata)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.sm_dark = QRadioButton(self.widget_9)
        self.sm_dark.setObjectName("sm_dark")

        self.horizontalLayout_28.addWidget(self.sm_dark)

        self.sm_light = QRadioButton(self.widget_9)
        self.sm_light.setObjectName("sm_light")

        self.horizontalLayout_28.addWidget(self.sm_light)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_11)

        self.gridLayout_10.addWidget(self.widget_9, 2, 3, 1, 1)

        self.sm_wafer_num = QLineEdit(self.sm_metadata)
        self.sm_wafer_num.setObjectName("sm_wafer_num")

        self.gridLayout_10.addWidget(self.sm_wafer_num, 0, 1, 1, 1)

        self.label_34 = QLabel(self.sm_metadata)
        self.label_34.setObjectName("label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_34, 0, 2, 1, 1)

        self.sm_comments = QTextEdit(self.sm_metadata)
        self.sm_comments.setObjectName("sm_comments")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sm_comments.sizePolicy().hasHeightForWidth())
        self.sm_comments.setSizePolicy(sizePolicy1)
        self.sm_comments.setMaximumSize(QSize(16777215, 50))
        self.sm_comments.setAutoFillBackground(True)

        self.gridLayout_10.addWidget(self.sm_comments, 4, 1, 1, 3)

        self.label_36 = QLabel(self.sm_metadata)
        self.label_36.setObjectName("label_36")

        self.gridLayout_10.addWidget(self.label_36, 4, 0, 1, 1)

        self.sm_data_path_button = QPushButton(self.sm_metadata)
        self.sm_data_path_button.setObjectName("sm_data_path_button")

        self.gridLayout_10.addWidget(self.sm_data_path_button, 5, 0, 1, 1)

        self.sm_data_path = QLabel(self.sm_metadata)
        self.sm_data_path.setObjectName("sm_data_path")

        self.gridLayout_10.addWidget(self.sm_data_path, 5, 1, 1, 3)

        self.verticalLayout_20.addLayout(self.gridLayout_10)

        self.verticalLayout_6.addWidget(self.sm_metadata)

        self.sm_quick_measurement = QGroupBox(self.tab_sweep)
        self.sm_quick_measurement.setObjectName("sm_quick_measurement")
        self._2 = QVBoxLayout(self.sm_quick_measurement)
        self._2.setObjectName("_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_17 = QLabel(self.sm_quick_measurement)
        self.label_17.setObjectName("label_17")

        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 1)

        self.sm_quick_measurement_sweep_step = QDoubleSpinBox(self.sm_quick_measurement)
        self.sm_quick_measurement_sweep_step.setObjectName("sm_quick_measurement_sweep_step")
        self.sm_quick_measurement_sweep_step.setDecimals(6)
        self.sm_quick_measurement_sweep_step.setMinimum(0.001000000000000)
        self.sm_quick_measurement_sweep_step.setMaximum(999.000000000000000)
        self.sm_quick_measurement_sweep_step.setSingleStep(0.000001000000000)
        self.sm_quick_measurement_sweep_step.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_quick_measurement_sweep_step.setValue(0.200000000000000)

        self.gridLayout_5.addWidget(self.sm_quick_measurement_sweep_step, 0, 1, 1, 1)

        self.label_16 = QLabel(self.sm_quick_measurement)
        self.label_16.setObjectName("label_16")

        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 1)

        self.sm_quick_measurement_pause = QDoubleSpinBox(self.sm_quick_measurement)
        self.sm_quick_measurement_pause.setObjectName("sm_quick_measurement_pause")
        self.sm_quick_measurement_pause.setDecimals(6)
        self.sm_quick_measurement_pause.setMaximum(9999.000000000000000)
        self.sm_quick_measurement_pause.setSingleStep(0.000001000000000)
        self.sm_quick_measurement_pause.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_quick_measurement_pause.setValue(0.100000000000000)

        self.gridLayout_5.addWidget(self.sm_quick_measurement_pause, 1, 1, 1, 1)

        self._2.addLayout(self.gridLayout_5)

        self.sm_quick_measurement_run = QPushButton(self.sm_quick_measurement)
        self.sm_quick_measurement_run.setObjectName("sm_quick_measurement_run")

        self._2.addWidget(self.sm_quick_measurement_run)

        self.verticalLayout_6.addWidget(self.sm_quick_measurement)

        self.sm_measurement = QGroupBox(self.tab_sweep)
        self.sm_measurement.setObjectName("sm_measurement")
        self._3 = QVBoxLayout(self.sm_measurement)
        self._3.setObjectName("_3")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_18 = QLabel(self.sm_measurement)
        self.label_18.setObjectName("label_18")

        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_19 = QLabel(self.sm_measurement)
        self.label_19.setObjectName("label_19")

        self.gridLayout_6.addWidget(self.label_19, 2, 0, 1, 1)

        self.sm_sweep_count = QSpinBox(self.sm_measurement)
        self.sm_sweep_count.setObjectName("sm_sweep_count")
        self.sm_sweep_count.setMinimum(1)
        self.sm_sweep_count.setValue(2)

        self.gridLayout_6.addWidget(self.sm_sweep_count, 0, 1, 1, 1)

        self.sm_measurement_pause = QDoubleSpinBox(self.sm_measurement)
        self.sm_measurement_pause.setObjectName("sm_measurement_pause")
        self.sm_measurement_pause.setDecimals(6)
        self.sm_measurement_pause.setMaximum(9999.000000000000000)
        self.sm_measurement_pause.setSingleStep(0.000001000000000)
        self.sm_measurement_pause.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_measurement_pause.setValue(0.100000000000000)

        self.gridLayout_6.addWidget(self.sm_measurement_pause, 2, 1, 1, 1)

        self.label_41 = QLabel(self.sm_measurement)
        self.label_41.setObjectName("label_41")

        self.gridLayout_6.addWidget(self.label_41, 1, 0, 1, 1)

        self.sm_sweep_pause = QDoubleSpinBox(self.sm_measurement)
        self.sm_sweep_pause.setObjectName("sm_sweep_pause")
        self.sm_sweep_pause.setDecimals(6)
        self.sm_sweep_pause.setMaximum(9999.000000000000000)
        self.sm_sweep_pause.setSingleStep(0.000001000000000)
        self.sm_sweep_pause.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_sweep_pause.setValue(0.010000000000000)

        self.gridLayout_6.addWidget(self.sm_sweep_pause, 1, 1, 1, 1)

        self._3.addLayout(self.gridLayout_6)

        self.sm_measurement_run = QPushButton(self.sm_measurement)
        self.sm_measurement_run.setObjectName("sm_measurement_run")

        self._3.addWidget(self.sm_measurement_run)

        self.verticalLayout_6.addWidget(self.sm_measurement)

        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sm_smu_config = QGroupBox(self.tab_sweep)
        self.sm_smu_config.setObjectName("sm_smu_config")
        self.verticalLayout_11 = QVBoxLayout(self.sm_smu_config)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_6 = QLabel(self.sm_smu_config)
        self.label_6.setObjectName("label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.smu_select_sm_1 = QComboBox(self.sm_smu_config)
        self.smu_select_sm_1.addItem("")
        self.smu_select_sm_1.setObjectName("smu_select_sm_1")

        self.verticalLayout_10.addWidget(self.smu_select_sm_1)

        self.widget_2 = QWidget(self.sm_smu_config)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.sm_voltage_1 = QRadioButton(self.widget_2)
        self.sm_voltage_1.setObjectName("sm_voltage_1")
        self.sm_voltage_1.setChecked(True)

        self.horizontalLayout_13.addWidget(self.sm_voltage_1)

        self.sm_current_1 = QRadioButton(self.widget_2)
        self.sm_current_1.setObjectName("sm_current_1")

        self.horizontalLayout_13.addWidget(self.sm_current_1)

        self.verticalLayout_10.addWidget(self.widget_2)

        self.horizontalLayout_7.addLayout(self.verticalLayout_10)

        self.line_2 = QFrame(self.sm_smu_config)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_13 = QLabel(self.sm_smu_config)
        self.label_13.setObjectName("label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_13)

        self.smu_select_sm_2 = QComboBox(self.sm_smu_config)
        self.smu_select_sm_2.addItem("")
        self.smu_select_sm_2.setObjectName("smu_select_sm_2")

        self.verticalLayout_4.addWidget(self.smu_select_sm_2)

        self.widget_10 = QWidget(self.sm_smu_config)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.sm_voltage_2 = QRadioButton(self.widget_10)
        self.sm_voltage_2.setObjectName("sm_voltage_2")
        self.sm_voltage_2.setChecked(True)

        self.horizontalLayout_14.addWidget(self.sm_voltage_2)

        self.sm_current_2 = QRadioButton(self.widget_10)
        self.sm_current_2.setObjectName("sm_current_2")

        self.horizontalLayout_14.addWidget(self.sm_current_2)

        self.verticalLayout_4.addWidget(self.widget_10)

        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.line = QFrame(self.sm_smu_config)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line)

        self.widget_11 = QWidget(self.sm_smu_config)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.sm_sweep_1 = QRadioButton(self.widget_11)
        self.sm_sweep_1.setObjectName("sm_sweep_1")
        self.sm_sweep_1.setChecked(True)

        self.horizontalLayout_10.addWidget(self.sm_sweep_1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.line_3 = QFrame(self.widget_11)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.sm_sweep_2 = QRadioButton(self.widget_11)
        self.sm_sweep_2.setObjectName("sm_sweep_2")

        self.horizontalLayout_10.addWidget(self.sm_sweep_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.verticalLayout_11.addWidget(self.widget_11)

        self.verticalLayout_2.addWidget(self.sm_smu_config)

        self.sm_sweep_params = QGroupBox(self.tab_sweep)
        self.sm_sweep_params.setObjectName("sm_sweep_params")
        self.verticalLayout_5 = QVBoxLayout(self.sm_sweep_params)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.sweep_start_label_2 = QLabel(self.sm_sweep_params)
        self.sweep_start_label_2.setObjectName("sweep_start_label_2")
        self.sweep_start_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.sweep_start_label_2, 0, 0, 1, 1)

        self.sweep_step_label_2 = QLabel(self.sm_sweep_params)
        self.sweep_step_label_2.setObjectName("sweep_step_label_2")
        self.sweep_step_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.sweep_step_label_2, 0, 1, 1, 1)

        self.sweep_end_label_2 = QLabel(self.sm_sweep_params)
        self.sweep_end_label_2.setObjectName("sweep_end_label_2")
        self.sweep_end_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.sweep_end_label_2, 0, 2, 1, 1)

        self.sm_sweep_step = QDoubleSpinBox(self.sm_sweep_params)
        self.sm_sweep_step.setObjectName("sm_sweep_step")
        self.sm_sweep_step.setDecimals(6)
        self.sm_sweep_step.setMinimum(0.001000000000000)
        self.sm_sweep_step.setMaximum(999.000000000000000)
        self.sm_sweep_step.setSingleStep(0.000001000000000)
        self.sm_sweep_step.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_sweep_step.setValue(0.010000000000000)

        self.gridLayout_11.addWidget(self.sm_sweep_step, 1, 1, 1, 1)

        self.sm_sweep_end = QDoubleSpinBox(self.sm_sweep_params)
        self.sm_sweep_end.setObjectName("sm_sweep_end")
        self.sm_sweep_end.setDecimals(6)
        self.sm_sweep_end.setMinimum(-1100.000000000000000)
        self.sm_sweep_end.setMaximum(1100.000000000000000)
        self.sm_sweep_end.setSingleStep(0.000001000000000)
        self.sm_sweep_end.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_sweep_end.setValue(1.500000000000000)

        self.gridLayout_11.addWidget(self.sm_sweep_end, 1, 2, 1, 1)

        self.sm_sweep_start = QDoubleSpinBox(self.sm_sweep_params)
        self.sm_sweep_start.setObjectName("sm_sweep_start")
        self.sm_sweep_start.setDecimals(6)
        self.sm_sweep_start.setMinimum(-1100.000000000000000)
        self.sm_sweep_start.setMaximum(1100.000000000000000)
        self.sm_sweep_start.setSingleStep(0.000001000000000)
        self.sm_sweep_start.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_sweep_start.setValue(-1.500000000000000)

        self.gridLayout_11.addWidget(self.sm_sweep_start, 1, 0, 1, 1)

        self.verticalLayout_5.addLayout(self.gridLayout_11)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.compliance_label_2 = QLabel(self.sm_sweep_params)
        self.compliance_label_2.setObjectName("compliance_label_2")

        self.horizontalLayout_11.addWidget(self.compliance_label_2)

        self.sm_sweep_compliance = QDoubleSpinBox(self.sm_sweep_params)
        self.sm_sweep_compliance.setObjectName("sm_sweep_compliance")
        self.sm_sweep_compliance.setEnabled(True)
        self.sm_sweep_compliance.setDecimals(6)
        self.sm_sweep_compliance.setMinimum(-1100.000000000000000)
        self.sm_sweep_compliance.setMaximum(1100.000000000000000)
        self.sm_sweep_compliance.setSingleStep(0.000001000000000)
        self.sm_sweep_compliance.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_sweep_compliance.setValue(-1.500000000000000)

        self.horizontalLayout_11.addWidget(self.sm_sweep_compliance)

        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.verticalLayout_2.addWidget(self.sm_sweep_params)

        self.sm_constant_params = QGroupBox(self.tab_sweep)
        self.sm_constant_params.setObjectName("sm_constant_params")
        self.verticalLayout_9 = QVBoxLayout(self.sm_constant_params)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.compliance_label_3 = QLabel(self.sm_constant_params)
        self.compliance_label_3.setObjectName("compliance_label_3")

        self.horizontalLayout_12.addWidget(self.compliance_label_3)

        self.sm_constant_output = QDoubleSpinBox(self.sm_constant_params)
        self.sm_constant_output.setObjectName("sm_constant_output")
        self.sm_constant_output.setEnabled(True)
        self.sm_constant_output.setDecimals(6)
        self.sm_constant_output.setMinimum(-1100.000000000000000)
        self.sm_constant_output.setMaximum(1100.000000000000000)
        self.sm_constant_output.setSingleStep(0.000001000000000)
        self.sm_constant_output.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_constant_output.setValue(-1.500000000000000)

        self.horizontalLayout_12.addWidget(self.sm_constant_output)

        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.compliance_label_4 = QLabel(self.sm_constant_params)
        self.compliance_label_4.setObjectName("compliance_label_4")

        self.horizontalLayout_30.addWidget(self.compliance_label_4)

        self.sm_constant_compliance = QDoubleSpinBox(self.sm_constant_params)
        self.sm_constant_compliance.setObjectName("sm_constant_compliance")
        self.sm_constant_compliance.setEnabled(True)
        self.sm_constant_compliance.setDecimals(6)
        self.sm_constant_compliance.setMinimum(-1061.000000000000000)
        self.sm_constant_compliance.setMaximum(1100.000000000000000)
        self.sm_constant_compliance.setSingleStep(0.000001000000000)
        self.sm_constant_compliance.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sm_constant_compliance.setValue(-1.500000000000000)

        self.horizontalLayout_30.addWidget(self.sm_constant_compliance)

        self.verticalLayout_9.addLayout(self.horizontalLayout_30)

        self.verticalLayout_2.addWidget(self.sm_constant_params)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sm_stop = QPushButton(self.tab_sweep)
        self.sm_stop.setObjectName("sm_stop")
        self.sm_stop.setEnabled(False)
        self.sm_stop.setMinimumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.sm_stop, 0, 0, 1, 1)

        self.sm_save_data = QPushButton(self.tab_sweep)
        self.sm_save_data.setObjectName("sm_save_data")
        self.sm_save_data.setEnabled(False)
        self.sm_save_data.setMinimumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.sm_save_data, 0, 1, 1, 1)

        self.sm_plot_settings = QPushButton(self.tab_sweep)
        self.sm_plot_settings.setObjectName("sm_plot_settings")
        self.sm_plot_settings.setEnabled(True)
        self.sm_plot_settings.setMinimumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.sm_plot_settings, 0, 2, 1, 1)

        self.sm_progress = QProgressBar(self.tab_sweep)
        self.sm_progress.setObjectName("sm_progress")
        self.sm_progress.setValue(0)
        self.sm_progress.setTextVisible(False)

        self.gridLayout.addWidget(self.sm_progress, 1, 0, 1, 3)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.sm_plot_container = QWidget(self.tab_sweep)
        self.sm_plot_container.setObjectName("sm_plot_container")
        self.verticalLayout_21 = QVBoxLayout(self.sm_plot_container)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.sm_plot_container)

        self.tabWidget.addTab(self.tab_sweep, "")
        self.tab_stream = QWidget()
        self.tab_stream.setObjectName("tab_stream")
        self.verticalLayout_16 = QVBoxLayout(self.tab_stream)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ds_metadata = QGroupBox(self.tab_stream)
        self.ds_metadata.setObjectName("ds_metadata")
        sizePolicy.setHeightForWidth(self.ds_metadata.sizePolicy().hasHeightForWidth())
        self.ds_metadata.setSizePolicy(sizePolicy)
        self.verticalLayout_15 = QVBoxLayout(self.ds_metadata)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ds_chip_num = QLineEdit(self.ds_metadata)
        self.ds_chip_num.setObjectName("ds_chip_num")

        self.gridLayout_4.addWidget(self.ds_chip_num, 0, 3, 1, 1)

        self.label_23 = QLabel(self.ds_metadata)
        self.label_23.setObjectName("label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_23, 2, 0, 1, 1)

        self.label_38 = QLabel(self.ds_metadata)
        self.label_38.setObjectName("label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_38, 0, 0, 1, 1)

        self.label_39 = QLabel(self.ds_metadata)
        self.label_39.setObjectName("label_39")

        self.gridLayout_4.addWidget(self.label_39, 4, 0, 1, 1)

        self.label_40 = QLabel(self.ds_metadata)
        self.label_40.setObjectName("label_40")

        self.gridLayout_4.addWidget(self.label_40, 2, 2, 1, 1)

        self.widget_7 = QWidget(self.ds_metadata)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.ds_dark = QRadioButton(self.widget_7)
        self.ds_dark.setObjectName("ds_dark")

        self.horizontalLayout_25.addWidget(self.ds_dark)

        self.ds_light = QRadioButton(self.widget_7)
        self.ds_light.setObjectName("ds_light")

        self.horizontalLayout_25.addWidget(self.ds_light)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_7)

        self.gridLayout_4.addWidget(self.widget_7, 2, 3, 1, 1)

        self.label_24 = QLabel(self.ds_metadata)
        self.label_24.setObjectName("label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_24, 0, 2, 1, 1)

        self.ds_comments = QTextEdit(self.ds_metadata)
        self.ds_comments.setObjectName("ds_comments")
        self.ds_comments.setMinimumSize(QSize(0, 0))
        self.ds_comments.setMaximumSize(QSize(16777215, 50))
        self.ds_comments.setAutoFillBackground(True)

        self.gridLayout_4.addWidget(self.ds_comments, 4, 1, 1, 3)

        self.ds_step_of_process = QLineEdit(self.ds_metadata)
        self.ds_step_of_process.setObjectName("ds_step_of_process")

        self.gridLayout_4.addWidget(self.ds_step_of_process, 2, 1, 1, 1)

        self.ds_wafer_num = QLineEdit(self.ds_metadata)
        self.ds_wafer_num.setObjectName("ds_wafer_num")

        self.gridLayout_4.addWidget(self.ds_wafer_num, 0, 1, 1, 1)

        self.ds_data_path_button = QPushButton(self.ds_metadata)
        self.ds_data_path_button.setObjectName("ds_data_path_button")

        self.gridLayout_4.addWidget(self.ds_data_path_button, 5, 0, 1, 1)

        self.ds_data_path = QLabel(self.ds_metadata)
        self.ds_data_path.setObjectName("ds_data_path")

        self.gridLayout_4.addWidget(self.ds_data_path, 5, 1, 1, 3)

        self.verticalLayout_15.addLayout(self.gridLayout_4)

        self.horizontalLayout_2.addWidget(self.ds_metadata)

        self.ds_measurement_config = QGroupBox(self.tab_stream)
        self.ds_measurement_config.setObjectName("ds_measurement_config")
        self.horizontalLayout_29 = QHBoxLayout(self.ds_measurement_config)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.ds_continuous = QRadioButton(self.ds_measurement_config)
        self.ds_continuous.setObjectName("ds_continuous")
        self.ds_continuous.setChecked(True)

        self.verticalLayout_12.addWidget(self.ds_continuous)

        self.ds_fixed_num = QRadioButton(self.ds_measurement_config)
        self.ds_fixed_num.setObjectName("ds_fixed_num")
        self.ds_fixed_num.setChecked(False)

        self.verticalLayout_12.addWidget(self.ds_fixed_num)

        self.ds_fixed_duration = QRadioButton(self.ds_measurement_config)
        self.ds_fixed_duration.setObjectName("ds_fixed_duration")

        self.verticalLayout_12.addWidget(self.ds_fixed_duration)

        self.horizontalLayout_29.addLayout(self.verticalLayout_12)

        self.line_4 = QFrame(self.ds_measurement_config)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_29.addWidget(self.line_4)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ds_measurement_pause = QDoubleSpinBox(self.ds_measurement_config)
        self.ds_measurement_pause.setObjectName("ds_measurement_pause")
        self.ds_measurement_pause.setMinimumSize(QSize(100, 0))
        self.ds_measurement_pause.setDecimals(6)
        self.ds_measurement_pause.setMaximum(9999.000000000000000)
        self.ds_measurement_pause.setSingleStep(0.000001000000000)
        self.ds_measurement_pause.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.ds_measurement_pause.setValue(0.100000000000000)

        self.gridLayout_7.addWidget(self.ds_measurement_pause, 2, 1, 1, 1)

        self.ds_duration_label = QLabel(self.ds_measurement_config)
        self.ds_duration_label.setObjectName("ds_duration_label")
        self.ds_duration_label.setEnabled(False)

        self.gridLayout_7.addWidget(self.ds_duration_label, 0, 0, 1, 1)

        self.ds_duration = QDoubleSpinBox(self.ds_measurement_config)
        self.ds_duration.setObjectName("ds_duration")
        self.ds_duration.setEnabled(False)
        self.ds_duration.setMinimumSize(QSize(100, 0))
        self.ds_duration.setDecimals(6)
        self.ds_duration.setMaximum(9999.000000000000000)
        self.ds_duration.setSingleStep(0.000001000000000)
        self.ds_duration.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.ds_duration.setValue(10.000000000000000)

        self.gridLayout_7.addWidget(self.ds_duration, 0, 1, 1, 1)

        self.label_21 = QLabel(self.ds_measurement_config)
        self.label_21.setObjectName("label_21")

        self.gridLayout_7.addWidget(self.label_21, 2, 0, 1, 1)

        self.ds_num_measurements = QSpinBox(self.ds_measurement_config)
        self.ds_num_measurements.setObjectName("ds_num_measurements")
        self.ds_num_measurements.setEnabled(False)
        self.ds_num_measurements.setMinimumSize(QSize(100, 0))
        self.ds_num_measurements.setMinimum(1)
        self.ds_num_measurements.setValue(2)

        self.gridLayout_7.addWidget(self.ds_num_measurements, 1, 1, 1, 1)

        self.ds_num_measurements_label = QLabel(self.ds_measurement_config)
        self.ds_num_measurements_label.setObjectName("ds_num_measurements_label")
        self.ds_num_measurements_label.setEnabled(False)

        self.gridLayout_7.addWidget(self.ds_num_measurements_label, 1, 0, 1, 1)

        self.horizontalLayout_29.addLayout(self.gridLayout_7)

        self.horizontalLayout_2.addWidget(self.ds_measurement_config)

        self.verticalLayout_16.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.ds_smu_1_config = QGroupBox(self.tab_stream)
        self.ds_smu_1_config.setObjectName("ds_smu_1_config")
        sizePolicy.setHeightForWidth(self.ds_smu_1_config.sizePolicy().hasHeightForWidth())
        self.ds_smu_1_config.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.ds_smu_1_config)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QLabel(self.ds_smu_1_config)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.smu_select_ds_1 = QComboBox(self.ds_smu_1_config)
        self.smu_select_ds_1.addItem("")
        self.smu_select_ds_1.setObjectName("smu_select_ds_1")
        self.smu_select_ds_1.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_9.addWidget(self.smu_select_ds_1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.widget_4 = QWidget(self.ds_smu_1_config)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.ds_voltage_1 = QRadioButton(self.widget_4)
        self.ds_voltage_1.setObjectName("ds_voltage_1")
        self.ds_voltage_1.setChecked(True)

        self.horizontalLayout_15.addWidget(self.ds_voltage_1)

        self.ds_current_1 = QRadioButton(self.widget_4)
        self.ds_current_1.setObjectName("ds_current_1")

        self.horizontalLayout_15.addWidget(self.ds_current_1)

        self.verticalLayout_3.addWidget(self.widget_4)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.compliance_label_8 = QLabel(self.ds_smu_1_config)
        self.compliance_label_8.setObjectName("compliance_label_8")

        self.horizontalLayout_19.addWidget(self.compliance_label_8)

        self.ds_output_1 = QDoubleSpinBox(self.ds_smu_1_config)
        self.ds_output_1.setObjectName("ds_output_1")
        self.ds_output_1.setEnabled(True)
        self.ds_output_1.setMinimumSize(QSize(100, 0))
        self.ds_output_1.setDecimals(6)
        self.ds_output_1.setMinimum(-1100.000000000000000)
        self.ds_output_1.setMaximum(1100.000000000000000)
        self.ds_output_1.setSingleStep(0.000001000000000)
        self.ds_output_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.ds_output_1.setValue(1.500000000000000)

        self.horizontalLayout_19.addWidget(self.ds_output_1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.compliance_label_7 = QLabel(self.ds_smu_1_config)
        self.compliance_label_7.setObjectName("compliance_label_7")

        self.horizontalLayout_18.addWidget(self.compliance_label_7)

        self.ds_compliance_1 = QDoubleSpinBox(self.ds_smu_1_config)
        self.ds_compliance_1.setObjectName("ds_compliance_1")
        self.ds_compliance_1.setEnabled(True)
        self.ds_compliance_1.setMinimumSize(QSize(100, 0))
        self.ds_compliance_1.setDecimals(6)
        self.ds_compliance_1.setMinimum(-1100.000000000000000)
        self.ds_compliance_1.setMaximum(1100.000000000000000)
        self.ds_compliance_1.setSingleStep(0.000001000000000)
        self.ds_compliance_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.ds_compliance_1.setValue(0.010000000000000)

        self.horizontalLayout_18.addWidget(self.ds_compliance_1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_22.addWidget(self.ds_smu_1_config)

        self.ds_smu_2_config = QGroupBox(self.tab_stream)
        self.ds_smu_2_config.setObjectName("ds_smu_2_config")
        sizePolicy.setHeightForWidth(self.ds_smu_2_config.sizePolicy().hasHeightForWidth())
        self.ds_smu_2_config.setSizePolicy(sizePolicy)
        self.verticalLayout_14 = QVBoxLayout(self.ds_smu_2_config)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_7 = QLabel(self.ds_smu_2_config)
        self.label_7.setObjectName("label_7")

        self.horizontalLayout_16.addWidget(self.label_7)

        self.smu_select_ds_2 = QComboBox(self.ds_smu_2_config)
        self.smu_select_ds_2.addItem("")
        self.smu_select_ds_2.setObjectName("smu_select_ds_2")
        self.smu_select_ds_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_16.addWidget(self.smu_select_ds_2)

        self.verticalLayout_14.addLayout(self.horizontalLayout_16)

        self.widget_6 = QWidget(self.ds_smu_2_config)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.ds_voltage_2 = QRadioButton(self.widget_6)
        self.ds_voltage_2.setObjectName("ds_voltage_2")
        self.ds_voltage_2.setChecked(True)

        self.horizontalLayout_21.addWidget(self.ds_voltage_2)

        self.ds_current_2 = QRadioButton(self.widget_6)
        self.ds_current_2.setObjectName("ds_current_2")

        self.horizontalLayout_21.addWidget(self.ds_current_2)

        self.verticalLayout_14.addWidget(self.widget_6)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.compliance_label_9 = QLabel(self.ds_smu_2_config)
        self.compliance_label_9.setObjectName("compliance_label_9")

        self.horizontalLayout_23.addWidget(self.compliance_label_9)

        self.ds_output_2 = QDoubleSpinBox(self.ds_smu_2_config)
        self.ds_output_2.setObjectName("ds_output_2")
        self.ds_output_2.setEnabled(True)
        self.ds_output_2.setMinimumSize(QSize(100, 0))
        self.ds_output_2.setDecimals(6)
        self.ds_output_2.setMinimum(-1100.000000000000000)
        self.ds_output_2.setMaximum(1100.000000000000000)
        self.ds_output_2.setSingleStep(0.000001000000000)
        self.ds_output_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.ds_output_2.setValue(1.500000000000000)

        self.horizontalLayout_23.addWidget(self.ds_output_2)

        self.verticalLayout_14.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.compliance_label_10 = QLabel(self.ds_smu_2_config)
        self.compliance_label_10.setObjectName("compliance_label_10")

        self.horizontalLayout_24.addWidget(self.compliance_label_10)

        self.ds_compliance_2 = QDoubleSpinBox(self.ds_smu_2_config)
        self.ds_compliance_2.setObjectName("ds_compliance_2")
        self.ds_compliance_2.setEnabled(True)
        self.ds_compliance_2.setMinimumSize(QSize(100, 0))
        self.ds_compliance_2.setDecimals(6)
        self.ds_compliance_2.setMinimum(-1100.000000000000000)
        self.ds_compliance_2.setMaximum(1100.000000000000000)
        self.ds_compliance_2.setSingleStep(0.000001000000000)
        self.ds_compliance_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.ds_compliance_2.setValue(0.010000000000000)

        self.horizontalLayout_24.addWidget(self.ds_compliance_2)

        self.verticalLayout_14.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_22.addWidget(self.ds_smu_2_config)

        self.verticalLayout_16.addLayout(self.horizontalLayout_22)

        self.widget_3 = QWidget(self.tab_stream)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_8 = QGridLayout(self.widget_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.ds_stream = QPushButton(self.widget_3)
        self.ds_stream.setObjectName("ds_stream")
        self.ds_stream.setEnabled(True)

        self.gridLayout_8.addWidget(self.ds_stream, 1, 0, 1, 1)

        self.ds_save_data = QPushButton(self.widget_3)
        self.ds_save_data.setObjectName("ds_save_data")
        self.ds_save_data.setEnabled(False)

        self.gridLayout_8.addWidget(self.ds_save_data, 1, 1, 1, 1)

        self.ds_plot_settings = QPushButton(self.widget_3)
        self.ds_plot_settings.setObjectName("ds_plot_settings")
        self.ds_plot_settings.setEnabled(True)

        self.gridLayout_8.addWidget(self.ds_plot_settings, 1, 2, 1, 1)

        self.ds_progress = QProgressBar(self.widget_3)
        self.ds_progress.setObjectName("ds_progress")
        self.ds_progress.setValue(0)
        self.ds_progress.setTextVisible(False)

        self.gridLayout_8.addWidget(self.ds_progress, 2, 0, 1, 3)

        self.verticalLayout_16.addWidget(self.widget_3)

        self.ds_plot_container = QWidget(self.tab_stream)
        self.ds_plot_container.setObjectName("ds_plot_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ds_plot_container.sizePolicy().hasHeightForWidth())
        self.ds_plot_container.setSizePolicy(sizePolicy2)
        self.verticalLayout_22 = QVBoxLayout(self.ds_plot_container)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_16.addWidget(self.ds_plot_container)

        self.tabWidget.addTab(self.tab_stream, "")
        self.tab_config = QWidget()
        self.tab_config.setObjectName("tab_config")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_config)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QLabel(self.tab_config)
        self.label.setObjectName("label")
        self.label.setMaximumSize(QSize(600, 400))
        self.label.setPixmap(QPixmap("device_diagram.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label)

        self.tabWidget.addTab(self.tab_config, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.smu_connections.setTitle(QCoreApplication.translate("MainWindow", "Connections", None))
        self.smu_disconnect.setText(QCoreApplication.translate("MainWindow", "Disconnect", None))
        self.smu_identify.setText(QCoreApplication.translate("MainWindow", "Identify", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", "Connect to Sourcemeters", None))
        self.smu_search.setText(QCoreApplication.translate("MainWindow", "Search for SMUs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_connect), QCoreApplication.translate("MainWindow", "Sourcemeter Connections", None))
        self.sm_metadata.setTitle(QCoreApplication.translate("MainWindow", "Metadata", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", "Step of Process:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", "Light:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", "Wafer #:", None))
        self.sm_dark.setText(QCoreApplication.translate("MainWindow", "Dark", None))
        self.sm_light.setText(QCoreApplication.translate("MainWindow", "Light", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", "Chip #:", None))
        self.sm_comments.setPlaceholderText(QCoreApplication.translate("MainWindow", "Enter a comments here...", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", "Comments:", None))
        self.sm_data_path_button.setText(QCoreApplication.translate("MainWindow", "File Output", None))
        self.sm_data_path.setText(QCoreApplication.translate("MainWindow", "No data save location specified", None))
        self.sm_quick_measurement.setTitle(QCoreApplication.translate("MainWindow", "Quick Measurement Parameters", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", "Sweep Step Override", None))
        self.sm_quick_measurement_sweep_step.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", "Pause Between Measurements", None))
        self.sm_quick_measurement_pause.setSuffix(QCoreApplication.translate("MainWindow", " s", None))
        self.sm_quick_measurement_run.setText(QCoreApplication.translate("MainWindow", "Run Quick Measurement", None))
        self.sm_measurement.setTitle(QCoreApplication.translate("MainWindow", "Measurement Parameters", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", "Number of Sweeps", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", "Pause Between Measurements", None))
        self.sm_measurement_pause.setSuffix(QCoreApplication.translate("MainWindow", " s", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", "Pause Between Sweeps", None))
        self.sm_sweep_pause.setSuffix(QCoreApplication.translate("MainWindow", " s", None))
        self.sm_measurement_run.setText(QCoreApplication.translate("MainWindow", "Run Measurements", None))
        self.sm_smu_config.setTitle(QCoreApplication.translate("MainWindow", "Sourcemeter Configurations", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "SMU 1", None))
        self.smu_select_sm_1.setItemText(0, QCoreApplication.translate("MainWindow", "Simulated", None))

        self.sm_voltage_1.setText(QCoreApplication.translate("MainWindow", "Voltage", None))
        self.sm_current_1.setText(QCoreApplication.translate("MainWindow", "Current", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", "SMU 2", None))
        self.smu_select_sm_2.setItemText(0, QCoreApplication.translate("MainWindow", "Simulated", None))

        self.sm_voltage_2.setText(QCoreApplication.translate("MainWindow", "Voltage", None))
        self.sm_current_2.setText(QCoreApplication.translate("MainWindow", "Current", None))
        self.sm_sweep_1.setText(QCoreApplication.translate("MainWindow", "Sweep", None))
        self.sm_sweep_2.setText(QCoreApplication.translate("MainWindow", "Sweep", None))
        self.sm_sweep_params.setTitle(QCoreApplication.translate("MainWindow", "Sweep Parameters", None))
        self.sm_sweep_params.setProperty("test", QCoreApplication.translate("MainWindow", "A, F, D", None))
        self.sweep_start_label_2.setText(QCoreApplication.translate("MainWindow", "Start", None))
        self.sweep_step_label_2.setText(QCoreApplication.translate("MainWindow", "Step", None))
        self.sweep_end_label_2.setText(QCoreApplication.translate("MainWindow", "End", None))
        self.sm_sweep_step.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.sm_sweep_end.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.sm_sweep_start.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.compliance_label_2.setText(QCoreApplication.translate("MainWindow", "Compliance", None))
        self.sm_sweep_compliance.setSuffix(QCoreApplication.translate("MainWindow", " A", None))
        self.sm_constant_params.setTitle(QCoreApplication.translate("MainWindow", "Constant Supply Parameters", None))
        self.sm_constant_params.setProperty("test", QCoreApplication.translate("MainWindow", "A, F, D", None))
        self.compliance_label_3.setText(QCoreApplication.translate("MainWindow", "Output", None))
        self.sm_constant_output.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.compliance_label_4.setText(QCoreApplication.translate("MainWindow", "Compliance", None))
        self.sm_constant_compliance.setSuffix(QCoreApplication.translate("MainWindow", " A", None))
        self.sm_stop.setText(QCoreApplication.translate("MainWindow", "Stop Measurement", None))
        self.sm_save_data.setText(QCoreApplication.translate("MainWindow", "Save Last Run", None))
        self.sm_plot_settings.setText(QCoreApplication.translate("MainWindow", "Plot settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sweep), QCoreApplication.translate("MainWindow", "Sweep Measurement", None))
        self.ds_metadata.setTitle(QCoreApplication.translate("MainWindow", "Metadata", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", "Step of Process:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", "Wafer #:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", "Comments:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", "Light:", None))
        self.ds_dark.setText(QCoreApplication.translate("MainWindow", "Dark", None))
        self.ds_light.setText(QCoreApplication.translate("MainWindow", "Light", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", "Chip #:", None))
        self.ds_comments.setPlaceholderText(QCoreApplication.translate("MainWindow", "Enter a comments here...", None))
        self.ds_data_path_button.setText(QCoreApplication.translate("MainWindow", "File Output", None))
        self.ds_data_path.setText(QCoreApplication.translate("MainWindow", "No data save location specified", None))
        self.ds_measurement_config.setTitle(QCoreApplication.translate("MainWindow", "Measurement Mode", None))
        self.ds_continuous.setText(QCoreApplication.translate("MainWindow", "Continuous", None))
        self.ds_fixed_num.setText(QCoreApplication.translate("MainWindow", "Fixed number", None))
        self.ds_fixed_duration.setText(QCoreApplication.translate("MainWindow", "Fixed duration", None))
        self.ds_measurement_pause.setSuffix(QCoreApplication.translate("MainWindow", " s", None))
        self.ds_duration_label.setText(QCoreApplication.translate("MainWindow", "Total Duration", None))
        self.ds_duration.setSuffix(QCoreApplication.translate("MainWindow", " s", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", "Pause Between Measurements", None))
        self.ds_num_measurements_label.setText(QCoreApplication.translate("MainWindow", "Number of Measurements", None))
        self.ds_smu_1_config.setTitle(QCoreApplication.translate("MainWindow", "SMU 1 Configuration", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Sourcemeter:", None))
        self.smu_select_ds_1.setItemText(0, QCoreApplication.translate("MainWindow", "Simulated", None))

        self.ds_voltage_1.setText(QCoreApplication.translate("MainWindow", "Voltage", None))
        self.ds_current_1.setText(QCoreApplication.translate("MainWindow", "Current", None))
        self.compliance_label_8.setText(QCoreApplication.translate("MainWindow", "Output", None))
        self.ds_output_1.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.compliance_label_7.setText(QCoreApplication.translate("MainWindow", "Compliance", None))
        self.ds_compliance_1.setSuffix(QCoreApplication.translate("MainWindow", " A", None))
        self.ds_smu_2_config.setTitle(QCoreApplication.translate("MainWindow", "SMU 2 Configuration", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Sourcemeter:", None))
        self.smu_select_ds_2.setItemText(0, QCoreApplication.translate("MainWindow", "Simulated", None))

        self.ds_voltage_2.setText(QCoreApplication.translate("MainWindow", "Voltage", None))
        self.ds_current_2.setText(QCoreApplication.translate("MainWindow", "Current", None))
        self.compliance_label_9.setText(QCoreApplication.translate("MainWindow", "Output", None))
        self.ds_output_2.setSuffix(QCoreApplication.translate("MainWindow", " V", None))
        self.compliance_label_10.setText(QCoreApplication.translate("MainWindow", "Compliance", None))
        self.ds_compliance_2.setSuffix(QCoreApplication.translate("MainWindow", " A", None))
        self.ds_stream.setText(QCoreApplication.translate("MainWindow", "Start Streaming", None))
        self.ds_save_data.setText(QCoreApplication.translate("MainWindow", "Save Last Run", None))
        self.ds_plot_settings.setText(QCoreApplication.translate("MainWindow", "Plot settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stream), QCoreApplication.translate("MainWindow", "Data Streaming", None))
        self.label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), QCoreApplication.translate("MainWindow", "Sourcemeter Configuration", None))

    # retranslateUi
