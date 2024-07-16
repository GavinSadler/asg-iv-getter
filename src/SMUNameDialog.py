from typing import Optional

import PySide6.QtWidgets as QtWidgets

from UserInterface.ui_smu_name_dialog import Ui_Dialog


class SMUNameDialog(QtWidgets.QDialog, Ui_Dialog):

    existing_name: Optional[str]

    def __init__(self, existing_name: Optional[str] = None, parent: Optional[QtWidgets.QWidget] = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.existing_name = existing_name

        if self.existing_name:
            self.name_edit.setText(existing_name)

    def get_name(self):

        if self.exec():
            if self.name_edit.text() == "":
                return self.existing_name

            return self.name_edit.text()
        else:
            return self.existing_name
