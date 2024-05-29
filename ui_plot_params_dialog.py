# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_plot_params_dialogGtzsRV.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, Qt, QTime, QUrl
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform,)
from PySide6.QtWidgets import QAbstractButton, QApplication, QDialog, QDialogButtonBox, QGroupBox, QHBoxLayout, QSizePolicy, QVBoxLayout, QWidget


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setModal(True)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.x_radio_group = QGroupBox(Dialog)
        self.x_radio_group.setObjectName(u"x_radio_group")
        self.verticalLayout = QVBoxLayout(self.x_radio_group)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addWidget(self.x_radio_group)

        self.y_radio_group = QGroupBox(Dialog)
        self.y_radio_group.setObjectName(u"y_radio_group")
        self.verticalLayout_2 = QVBoxLayout(self.y_radio_group)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addWidget(self.y_radio_group)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.x_radio_group.setTitle(QCoreApplication.translate("Dialog", u"X-Axis", None))
        self.y_radio_group.setTitle(QCoreApplication.translate("Dialog", u"Y-Axis", None))
    # retranslateUi

