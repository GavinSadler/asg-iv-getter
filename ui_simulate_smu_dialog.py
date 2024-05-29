# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulate_smu_dialogDZlqno.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, Qt, QTime, QUrl
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform,)
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QWidget


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(327, 146)
        Dialog.setMaximumSize(QSize(327, 146))
        self._2 = QVBoxLayout(Dialog)
        self._2.setObjectName(u"_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(Qt.TextFormat.PlainText)

        self._2.addWidget(self.label)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.button_yes = QPushButton(Dialog)
        self.button_yes.setObjectName(u"button_yes")

        self.hboxLayout.addWidget(self.button_yes)

        self.button_no = QPushButton(Dialog)
        self.button_no.setObjectName(u"button_no")

        self.hboxLayout.addWidget(self.button_no)


        self._2.addLayout(self.hboxLayout)


        self.retranslateUi(Dialog)
        self.button_no.clicked.connect(Dialog.reject)
        self.button_yes.clicked.connect(Dialog.accept)

        self.button_no.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Unable to connect to SMU(s)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"A connection could not be made with the following SMUs:\n"
"\n"
"SMU1\n"
"SMU2\n"
"\n"
"Would you like to simulate the SMU(s)?", None))
        self.button_yes.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.button_no.setText(QCoreApplication.translate("Dialog", u"No", None))
    # retranslateUi

