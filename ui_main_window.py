# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowIQxYkr.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(867, 880)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(550, 300))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 400, 250))
        self.label.setPixmap(QPixmap(u"device_diagram.png"))
        self.label.setScaledContents(True)
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(430, 60, 111, 191))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.smu_1_sn = QLabel(self.verticalLayoutWidget_2)
        self.smu_1_sn.setObjectName(u"smu_1_sn")

        self.verticalLayout_2.addWidget(self.smu_1_sn)

        self.smu_1_mode = QComboBox(self.verticalLayoutWidget_2)
        self.smu_1_mode.addItem("")
        self.smu_1_mode.addItem("")
        self.smu_1_mode.setObjectName(u"smu_1_mode")

        self.verticalLayout_2.addWidget(self.smu_1_mode)

        self.smu_1_supply = QComboBox(self.verticalLayoutWidget_2)
        self.smu_1_supply.addItem("")
        self.smu_1_supply.addItem("")
        self.smu_1_supply.setObjectName(u"smu_1_supply")

        self.verticalLayout_2.addWidget(self.smu_1_supply)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.smu_2_sn = QLabel(self.verticalLayoutWidget_2)
        self.smu_2_sn.setObjectName(u"smu_2_sn")

        self.verticalLayout_2.addWidget(self.smu_2_sn)

        self.smu_2_mode = QComboBox(self.verticalLayoutWidget_2)
        self.smu_2_mode.addItem("")
        self.smu_2_mode.addItem("")
        self.smu_2_mode.setObjectName(u"smu_2_mode")

        self.verticalLayout_2.addWidget(self.smu_2_mode)

        self.smu_2_supply = QComboBox(self.verticalLayoutWidget_2)
        self.smu_2_supply.addItem("")
        self.smu_2_supply.addItem("")
        self.smu_2_supply.setObjectName(u"smu_2_supply")

        self.verticalLayout_2.addWidget(self.smu_2_supply)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sourcemeter_config_group = QGroupBox(self.frame)
        self.sourcemeter_config_group.setObjectName(u"sourcemeter_config_group")
        self.verticalLayout = QVBoxLayout(self.sourcemeter_config_group)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sweep_step_1 = QDoubleSpinBox(self.sourcemeter_config_group)
        self.sweep_step_1.setObjectName(u"sweep_step_1")
        self.sweep_step_1.setDecimals(3)
        self.sweep_step_1.setMinimum(0.001000000000000)
        self.sweep_step_1.setMaximum(999.000000000000000)
        self.sweep_step_1.setSingleStep(0.001000000000000)
        self.sweep_step_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sweep_step_1.setValue(0.010000000000000)

        self.gridLayout_2.addWidget(self.sweep_step_1, 1, 1, 1, 1)

        self.sweep_start_label_1 = QLabel(self.sourcemeter_config_group)
        self.sweep_start_label_1.setObjectName(u"sweep_start_label_1")
        self.sweep_start_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.sweep_start_label_1, 0, 0, 1, 1)

        self.sweep_step_label_1 = QLabel(self.sourcemeter_config_group)
        self.sweep_step_label_1.setObjectName(u"sweep_step_label_1")
        self.sweep_step_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.sweep_step_label_1, 0, 1, 1, 1)

        self.sweep_start_1 = QDoubleSpinBox(self.sourcemeter_config_group)
        self.sweep_start_1.setObjectName(u"sweep_start_1")
        self.sweep_start_1.setDecimals(3)
        self.sweep_start_1.setMinimum(-1100.000000000000000)
        self.sweep_start_1.setMaximum(1100.000000000000000)
        self.sweep_start_1.setSingleStep(0.001000000000000)
        self.sweep_start_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sweep_start_1.setValue(-1.500000000000000)

        self.gridLayout_2.addWidget(self.sweep_start_1, 1, 0, 1, 1)

        self.sweep_end_label_1 = QLabel(self.sourcemeter_config_group)
        self.sweep_end_label_1.setObjectName(u"sweep_end_label_1")
        self.sweep_end_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.sweep_end_label_1, 0, 2, 1, 1)

        self.sweep_end_1 = QDoubleSpinBox(self.sourcemeter_config_group)
        self.sweep_end_1.setObjectName(u"sweep_end_1")
        self.sweep_end_1.setDecimals(3)
        self.sweep_end_1.setMinimum(-1100.000000000000000)
        self.sweep_end_1.setMaximum(1100.000000000000000)
        self.sweep_end_1.setSingleStep(0.001000000000000)
        self.sweep_end_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sweep_end_1.setValue(1.500000000000000)

        self.gridLayout_2.addWidget(self.sweep_end_1, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.supply_label_1 = QLabel(self.sourcemeter_config_group)
        self.supply_label_1.setObjectName(u"supply_label_1")
        self.supply_label_1.setEnabled(False)

        self.gridLayout.addWidget(self.supply_label_1, 0, 0, 1, 1)

        self.supply_1 = QDoubleSpinBox(self.sourcemeter_config_group)
        self.supply_1.setObjectName(u"supply_1")
        self.supply_1.setEnabled(False)
        self.supply_1.setDecimals(3)
        self.supply_1.setMinimum(-1100.000000000000000)
        self.supply_1.setMaximum(1100.000000000000000)
        self.supply_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.supply_1.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.supply_1, 0, 1, 1, 1)

        self.compliance_label_1 = QLabel(self.sourcemeter_config_group)
        self.compliance_label_1.setObjectName(u"compliance_label_1")

        self.gridLayout.addWidget(self.compliance_label_1, 1, 0, 1, 1)

        self.compliance_1 = QDoubleSpinBox(self.sourcemeter_config_group)
        self.compliance_1.setObjectName(u"compliance_1")
        self.compliance_1.setDecimals(3)
        self.compliance_1.setMinimum(-5.000000000000000)
        self.compliance_1.setMaximum(5.000000000000000)
        self.compliance_1.setSingleStep(0.001000000000000)
        self.compliance_1.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.compliance_1.setValue(0.020000000000000)

        self.gridLayout.addWidget(self.compliance_1, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_5.addWidget(self.sourcemeter_config_group)

        self.sourcemeter_config_group_2 = QGroupBox(self.frame)
        self.sourcemeter_config_group_2.setObjectName(u"sourcemeter_config_group_2")
        self.verticalLayout_4 = QVBoxLayout(self.sourcemeter_config_group_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sweep_start_label_2 = QLabel(self.sourcemeter_config_group_2)
        self.sweep_start_label_2.setObjectName(u"sweep_start_label_2")
        self.sweep_start_label_2.setEnabled(False)
        self.sweep_start_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.sweep_start_label_2, 0, 0, 1, 1)

        self.sweep_step_label_2 = QLabel(self.sourcemeter_config_group_2)
        self.sweep_step_label_2.setObjectName(u"sweep_step_label_2")
        self.sweep_step_label_2.setEnabled(False)
        self.sweep_step_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.sweep_step_label_2, 0, 1, 1, 1)

        self.sweep_end_label_2 = QLabel(self.sourcemeter_config_group_2)
        self.sweep_end_label_2.setObjectName(u"sweep_end_label_2")
        self.sweep_end_label_2.setEnabled(False)
        self.sweep_end_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.sweep_end_label_2, 0, 2, 1, 1)

        self.sweep_step_2 = QDoubleSpinBox(self.sourcemeter_config_group_2)
        self.sweep_step_2.setObjectName(u"sweep_step_2")
        self.sweep_step_2.setEnabled(False)
        self.sweep_step_2.setDecimals(3)
        self.sweep_step_2.setMinimum(0.001000000000000)
        self.sweep_step_2.setMaximum(999.000000000000000)
        self.sweep_step_2.setSingleStep(0.001000000000000)
        self.sweep_step_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sweep_step_2.setValue(0.010000000000000)

        self.gridLayout_3.addWidget(self.sweep_step_2, 1, 1, 1, 1)

        self.sweep_end_2 = QDoubleSpinBox(self.sourcemeter_config_group_2)
        self.sweep_end_2.setObjectName(u"sweep_end_2")
        self.sweep_end_2.setEnabled(False)
        self.sweep_end_2.setDecimals(3)
        self.sweep_end_2.setMinimum(-1100.000000000000000)
        self.sweep_end_2.setMaximum(1100.000000000000000)
        self.sweep_end_2.setSingleStep(0.001000000000000)
        self.sweep_end_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sweep_end_2.setValue(1.500000000000000)

        self.gridLayout_3.addWidget(self.sweep_end_2, 1, 2, 1, 1)

        self.sweep_start_2 = QDoubleSpinBox(self.sourcemeter_config_group_2)
        self.sweep_start_2.setObjectName(u"sweep_start_2")
        self.sweep_start_2.setEnabled(False)
        self.sweep_start_2.setDecimals(3)
        self.sweep_start_2.setMinimum(-1100.000000000000000)
        self.sweep_start_2.setMaximum(1100.000000000000000)
        self.sweep_start_2.setSingleStep(0.001000000000000)
        self.sweep_start_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sweep_start_2.setValue(-1.500000000000000)

        self.gridLayout_3.addWidget(self.sweep_start_2, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.supply_label_2 = QLabel(self.sourcemeter_config_group_2)
        self.supply_label_2.setObjectName(u"supply_label_2")
        self.supply_label_2.setEnabled(True)

        self.gridLayout_4.addWidget(self.supply_label_2, 0, 0, 1, 1)

        self.compliance_label_2 = QLabel(self.sourcemeter_config_group_2)
        self.compliance_label_2.setObjectName(u"compliance_label_2")

        self.gridLayout_4.addWidget(self.compliance_label_2, 1, 0, 1, 1)

        self.supply_2 = QDoubleSpinBox(self.sourcemeter_config_group_2)
        self.supply_2.setObjectName(u"supply_2")
        self.supply_2.setDecimals(3)
        self.supply_2.setMinimum(-5.000000000000000)
        self.supply_2.setMaximum(5.000000000000000)
        self.supply_2.setSingleStep(0.001000000000000)
        self.supply_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.supply_2.setValue(0.020000000000000)

        self.gridLayout_4.addWidget(self.supply_2, 0, 1, 1, 1)

        self.compliance_2 = QDoubleSpinBox(self.sourcemeter_config_group_2)
        self.compliance_2.setObjectName(u"compliance_2")
        self.compliance_2.setEnabled(True)
        self.compliance_2.setDecimals(3)
        self.compliance_2.setMinimum(-1100.000000000000000)
        self.compliance_2.setMaximum(1100.000000000000000)
        self.compliance_2.setSingleStep(0.001000000000000)
        self.compliance_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.compliance_2.setValue(-1.500000000000000)

        self.gridLayout_4.addWidget(self.compliance_2, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)


        self.verticalLayout_5.addWidget(self.sourcemeter_config_group_2)

        self.groupBox_6 = QGroupBox(self.frame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self._2 = QVBoxLayout(self.groupBox_6)
        self._2.setObjectName(u"_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 1)

        self.quick_measurement_sweep_step = QDoubleSpinBox(self.groupBox_6)
        self.quick_measurement_sweep_step.setObjectName(u"quick_measurement_sweep_step")
        self.quick_measurement_sweep_step.setDecimals(3)
        self.quick_measurement_sweep_step.setMinimum(0.001000000000000)
        self.quick_measurement_sweep_step.setMaximum(999.000000000000000)
        self.quick_measurement_sweep_step.setSingleStep(0.001000000000000)
        self.quick_measurement_sweep_step.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.quick_measurement_sweep_step.setValue(0.200000000000000)

        self.gridLayout_5.addWidget(self.quick_measurement_sweep_step, 0, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 1)

        self.quick_measurement_pause = QDoubleSpinBox(self.groupBox_6)
        self.quick_measurement_pause.setObjectName(u"quick_measurement_pause")
        self.quick_measurement_pause.setDecimals(2)
        self.quick_measurement_pause.setMaximum(9999.000000000000000)
        self.quick_measurement_pause.setSingleStep(0.100000000000000)
        self.quick_measurement_pause.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.quick_measurement_pause.setValue(0.010000000000000)

        self.gridLayout_5.addWidget(self.quick_measurement_pause, 1, 1, 1, 1)


        self._2.addLayout(self.gridLayout_5)

        self.quick_measurement_run = QPushButton(self.groupBox_6)
        self.quick_measurement_run.setObjectName(u"quick_measurement_run")

        self._2.addWidget(self.quick_measurement_run)


        self.verticalLayout_5.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.frame)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self._3 = QVBoxLayout(self.groupBox_7)
        self._3.setObjectName(u"_3")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_18 = QLabel(self.groupBox_7)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox_7)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 1, 0, 1, 1)

        self.quick_measurement_pause_2 = QDoubleSpinBox(self.groupBox_7)
        self.quick_measurement_pause_2.setObjectName(u"quick_measurement_pause_2")
        self.quick_measurement_pause_2.setDecimals(2)
        self.quick_measurement_pause_2.setMaximum(9999.000000000000000)
        self.quick_measurement_pause_2.setSingleStep(0.100000000000000)
        self.quick_measurement_pause_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.quick_measurement_pause_2.setValue(0.010000000000000)

        self.gridLayout_6.addWidget(self.quick_measurement_pause_2, 1, 1, 1, 1)

        self.quick_measurement_sweep_step_2 = QSpinBox(self.groupBox_7)
        self.quick_measurement_sweep_step_2.setObjectName(u"quick_measurement_sweep_step_2")
        self.quick_measurement_sweep_step_2.setMinimum(1)
        self.quick_measurement_sweep_step_2.setValue(2)

        self.gridLayout_6.addWidget(self.quick_measurement_sweep_step_2, 0, 1, 1, 1)


        self._3.addLayout(self.gridLayout_6)

        self.quick_measurement_run_2 = QPushButton(self.groupBox_7)
        self.quick_measurement_run_2.setObjectName(u"quick_measurement_run_2")

        self._3.addWidget(self.quick_measurement_run_2)


        self.verticalLayout_5.addWidget(self.groupBox_7)


        self.verticalLayout_6.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.graph_container = QVBoxLayout()
        self.graph_container.setObjectName(u"graph_container")

        self.horizontalLayout.addLayout(self.graph_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sourcemeter Configuration", None))
        self.label.setText("")
        self.smu_1_sn.setText(QCoreApplication.translate("MainWindow", u"SN: -", None))
        self.smu_1_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Sweep", None))
        self.smu_1_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Constant", None))

        self.smu_1_supply.setItemText(0, QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.smu_1_supply.setItemText(1, QCoreApplication.translate("MainWindow", u"Current", None))

        self.smu_2_sn.setText(QCoreApplication.translate("MainWindow", u"SN: -", None))
        self.smu_2_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Sweep", None))
        self.smu_2_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Constant", None))

        self.smu_2_mode.setCurrentText(QCoreApplication.translate("MainWindow", u"Sweep", None))
        self.smu_2_supply.setItemText(0, QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.smu_2_supply.setItemText(1, QCoreApplication.translate("MainWindow", u"Current", None))

        self.sourcemeter_config_group.setTitle(QCoreApplication.translate("MainWindow", u"Sourcemeter 1 Configuration - Sweep Voltage", None))
        self.sweep_step_1.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.sweep_start_label_1.setText(QCoreApplication.translate("MainWindow", u"Voltage Start", None))
        self.sweep_step_label_1.setText(QCoreApplication.translate("MainWindow", u"Voltage Step", None))
        self.sweep_start_1.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.sweep_end_label_1.setText(QCoreApplication.translate("MainWindow", u"Voltage End", None))
        self.sweep_end_1.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.supply_label_1.setText(QCoreApplication.translate("MainWindow", u"Voltage Supply", None))
        self.supply_1.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.compliance_label_1.setText(QCoreApplication.translate("MainWindow", u"Current Compliance", None))
        self.compliance_1.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.sourcemeter_config_group_2.setTitle(QCoreApplication.translate("MainWindow", u"Sourcemeter 2 Configuration - Constant Current", None))
        self.sourcemeter_config_group_2.setProperty("test", QCoreApplication.translate("MainWindow", u"A, F, D", None))
        self.sweep_start_label_2.setText(QCoreApplication.translate("MainWindow", u"Voltage Start", None))
        self.sweep_step_label_2.setText(QCoreApplication.translate("MainWindow", u"Voltage Step", None))
        self.sweep_end_label_2.setText(QCoreApplication.translate("MainWindow", u"Voltage End", None))
        self.sweep_step_2.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.sweep_end_2.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.sweep_start_2.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.supply_label_2.setText(QCoreApplication.translate("MainWindow", u"Current Supply", None))
        self.compliance_label_2.setText(QCoreApplication.translate("MainWindow", u"Voltage Compliance", None))
        self.supply_2.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.compliance_2.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Quick Measurement Parameters", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Sweep Step Override", None))
        self.quick_measurement_sweep_step.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Pause Between Measurements", None))
        self.quick_measurement_pause.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.quick_measurement_run.setText(QCoreApplication.translate("MainWindow", u"Run Quick Measurement", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Measurement Parameters", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Number of Measurements", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Pause Between Measurements", None))
        self.quick_measurement_pause_2.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.quick_measurement_run_2.setText(QCoreApplication.translate("MainWindow", u"Run Measurements", None))
    # retranslateUi

