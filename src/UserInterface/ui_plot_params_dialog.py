# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot_params_dialoguyNVUk.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import QDialogButtonBox, QGroupBox, QHBoxLayout, QVBoxLayout


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(174, 86)
        Dialog.setModal(True)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.x_radio_group = QGroupBox(Dialog)
        self.x_radio_group.setObjectName("x_radio_group")
        self.verticalLayout = QVBoxLayout(self.x_radio_group)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout.addWidget(self.x_radio_group)

        self.y_radio_group = QGroupBox(Dialog)
        self.y_radio_group.setObjectName("y_radio_group")
        self.verticalLayout_2 = QVBoxLayout(self.y_radio_group)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout.addWidget(self.y_radio_group)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Plot Parameters", None))
        self.x_radio_group.setTitle(QCoreApplication.translate("Dialog", "X-Axis", None))
        self.y_radio_group.setTitle(QCoreApplication.translate("Dialog", "Y-Axis", None))

    # retranslateUi
