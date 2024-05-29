# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress_dialoggfVoAP.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, Qt, QTime, QUrl
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform,)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QHBoxLayout, QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget,)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(450, 300)
        Dialog.setMinimumSize(QSize(450, 300))
        Dialog.setModal(True)
        self.vboxLayout = QVBoxLayout(Dialog)
        self.vboxLayout.setObjectName("vboxLayout")
        self.messages = QPlainTextEdit(Dialog)
        self.messages.setObjectName("messages")
        self.messages.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.messages.setReadOnly(True)

        self.vboxLayout.addWidget(self.messages)

        self.progress_bar = QProgressBar(Dialog)
        self.progress_bar.setObjectName("progress_bar")

        self.vboxLayout.addWidget(self.progress_bar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_cancel = QPushButton(Dialog)
        self.button_cancel.setObjectName("button_cancel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cancel.sizePolicy().hasHeightForWidth())
        self.button_cancel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.button_cancel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_confirm = QPushButton(Dialog)
        self.button_confirm.setObjectName("button_confirm")
        self.button_confirm.setEnabled(False)

        self.horizontalLayout.addWidget(self.button_confirm)

        self.vboxLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.button_cancel.clicked.connect(Dialog.reject)
        self.button_confirm.clicked.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.button_cancel.setText(QCoreApplication.translate("Dialog", "Cancel", None))
        self.button_confirm.setText(QCoreApplication.translate("Dialog", "Confirm", None))

    # retranslateUi
