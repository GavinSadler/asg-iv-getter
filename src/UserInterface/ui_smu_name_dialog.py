# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smu_name_dialogrOTxWK.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtWidgets import QDialogButtonBox, QGridLayout, QLineEdit


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(174, 70)
        Dialog.setMaximumSize(QSize(174, 70))
        Dialog.setModal(True)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.name_edit = QLineEdit(Dialog)
        self.name_edit.setObjectName("name_edit")

        self.gridLayout.addWidget(self.name_edit, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "SMU Name", None))
        self.name_edit.setPlaceholderText(QCoreApplication.translate("Dialog", "Sourcemeter name...", None))

    # retranslateUi
