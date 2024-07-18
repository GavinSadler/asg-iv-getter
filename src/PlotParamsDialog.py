from enum import Enum
from typing import List, Optional

from PySide6.QtWidgets import QDialog, QRadioButton

from UserInterface.ui_plot_params_dialog import Ui_Dialog


class PlotParam(Enum):
    smu_1_voltage = "smu_1_voltage"
    smu_1_current = "smu_1_current"
    smu_2_voltage = "smu_2_voltage"
    smu_2_current = "smu_2_current"
    time = "time"

    @staticmethod
    def strings() -> List[str]:
        return [p.name for p in PlotParam]


class PlotParamsDialog(QDialog, Ui_Dialog):

    x_radios: List[QRadioButton]
    y_radios: List[QRadioButton]

    def __init__(self, parent=None, x_selected: PlotParam = PlotParam.smu_1_voltage, y_selected: PlotParam = PlotParam.smu_1_current, smu_1_name: Optional[str] = None, smu_2_name: Optional[str] = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi(self)

        # Initialize fields
        self.x_radios: List[QRadioButton] = []
        self.y_radios: List[QRadioButton] = []
        self.smu_1_name = smu_1_name
        self.smu_2_name = smu_2_name

        # Add all the radio buttons
        for column in PlotParam.strings():

            if self.smu_1_name:
                label = column.replace("smu_1_", f"{self.smu_1_name} ")

            if self.smu_2_name:
                label = column.replace("smu_2_", f"{self.smu_2_name} ")

            x_radio = QRadioButton(label, self.x_radio_group)
            x_radio.param_str = column
            self.x_radios.append(x_radio)
            self.x_radio_group.layout().addWidget(x_radio)

            if x_radio.param_str == x_selected.name:
                x_radio.setChecked(True)

            y_radio = QRadioButton(label, self.y_radio_group)
            y_radio.param_str = column
            self.y_radios.append(y_radio)
            self.y_radio_group.layout().addWidget(y_radio)

            if y_radio.param_str == y_selected.name:
                y_radio.setChecked(True)

        self.adjustSize()
        self.setFixedSize(self.size())

        self.show()

    def get_params(self):

        if self.exec():
            for r in self.x_radios:
                if r.isChecked():
                    x_param = PlotParam[r.text()]

            for r in self.y_radios:
                if r.isChecked():
                    y_param = PlotParam[r.text()]

            return x_param, y_param

        return None


if __name__ == "__main__":

    import sys

    from PySide6.QtWidgets import QApplication

    # Create the application instance
    app = QApplication(sys.argv)

    print(PlotParamsDialog().get_params())

    # Enter the main event loop
    sys.exit(app.exec())
