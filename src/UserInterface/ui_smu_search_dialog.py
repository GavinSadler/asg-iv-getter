# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smu_search_dialogptNztL.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtWidgets import QAbstractScrollArea, QDialogButtonBox, QGridLayout, QGroupBox, QListWidget, QPlainTextEdit, QProgressBar, QPushButton, QVBoxLayout


class Ui_smu_search_dialog(object):
    def setupUi(self, smu_search_dialog):
        if not smu_search_dialog.objectName():
            smu_search_dialog.setObjectName("smu_search_dialog")
        smu_search_dialog.resize(650, 500)
        smu_search_dialog.setMinimumSize(QSize(650, 500))
        smu_search_dialog.setSizeGripEnabled(True)
        smu_search_dialog.setModal(True)
        self.gridLayout = QGridLayout(smu_search_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.smu_connections = QGroupBox(smu_search_dialog)
        self.smu_connections.setObjectName("smu_connections")
        self.gridLayout_2 = QGridLayout(self.smu_connections)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.smu_identify = QPushButton(self.smu_connections)
        self.smu_identify.setObjectName("smu_identify")
        self.smu_identify.setEnabled(False)

        self.gridLayout_2.addWidget(self.smu_identify, 1, 1, 1, 1)

        self.connection_list = QListWidget(self.smu_connections)
        self.connection_list.setObjectName("connection_list")

        self.gridLayout_2.addWidget(self.connection_list, 0, 0, 1, 2)

        self.smu_disconnect = QPushButton(self.smu_connections)
        self.smu_disconnect.setObjectName("smu_disconnect")
        self.smu_disconnect.setEnabled(False)

        self.gridLayout_2.addWidget(self.smu_disconnect, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.smu_connections, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(smu_search_dialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.search_log = QPlainTextEdit(self.groupBox_4)
        self.search_log.setObjectName("search_log")
        self.search_log.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.search_log.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.search_log)

        self.search_progress = QProgressBar(self.groupBox_4)
        self.search_progress.setObjectName("search_progress")

        self.verticalLayout_8.addWidget(self.search_progress)

        self.search = QPushButton(self.groupBox_4)
        self.search.setObjectName("search")
        self.search.setEnabled(True)

        self.verticalLayout_8.addWidget(self.search)

        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(smu_search_dialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(smu_search_dialog)
        self.buttonBox.clicked.connect(smu_search_dialog.accept)

        QMetaObject.connectSlotsByName(smu_search_dialog)

    # setupUi

    def retranslateUi(self, smu_search_dialog):
        smu_search_dialog.setWindowTitle(QCoreApplication.translate("smu_search_dialog", "SMU Connections", None))
        self.smu_connections.setTitle(QCoreApplication.translate("smu_search_dialog", "Connections", None))
        self.smu_identify.setText(QCoreApplication.translate("smu_search_dialog", "Identify", None))
        self.smu_disconnect.setText(QCoreApplication.translate("smu_search_dialog", "Disconnect", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("smu_search_dialog", "Connect to Sourcemeters", None))
        self.search.setText(QCoreApplication.translate("smu_search_dialog", "Search for SMUs", None))

    # retranslateUi
