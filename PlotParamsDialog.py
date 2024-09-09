from enum import Enum
from typing import Dict

from PySide6.QtWidgets import QDialog, QRadioButton

from ui_plot_params_dialog import Ui_Dialog


class PlotParam(Enum):
    smu_1_voltage = "smu_1_voltage"
    smu_1_current = "smu_1_current"
    smu_2_voltage = "smu_2_voltage"
    smu_2_current = "smu_2_current"
    time = "time"


class PlotParamsDialog(QDialog, Ui_Dialog):

    x_radios: Dict[QRadioButton, PlotParam]
    y_radios: Dict[QRadioButton, PlotParam]

    def __init__(
        self,
        parent=None,
        x_selected: PlotParam = PlotParam.smu_1_voltage,
        y_selected: PlotParam = PlotParam.smu_1_current,
        smu_1_name: str = "SMU 1",
        smu_2_name: str = "SMU 2",
    ):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi(self)

        # Initialize fields
        self.x_radios = {}
        self.y_radios = {}
        self.smu_1_name = smu_1_name
        self.smu_2_name = smu_2_name

        # Add all the radio buttons
        for p in PlotParam:

            label = (
                p.name.replace("smu_1_", f"{self.smu_1_name} ")
                .replace("smu_2_", f"{self.smu_2_name} ")
                .replace("voltage", "Voltage")
                .replace("current", "Current")
                .replace("time", "Time")
            )

            x_radio = QRadioButton(label, self.x_radio_group)
            self.x_radios[x_radio] = p
            self.x_radio_group.layout().addWidget(x_radio)

            if self.x_radios.get(x_radio) == x_selected:
                x_radio.setChecked(True)

            y_radio = QRadioButton(label, self.y_radio_group)
            self.y_radios[y_radio] = p
            self.y_radio_group.layout().addWidget(y_radio)

            if self.y_radios.get(y_radio) == y_selected:
                y_radio.setChecked(True)

        self.adjustSize()
        self.setFixedSize(self.size())

        self.show()

    def get_params(self):

        if self.exec():
            for r in self.x_radios:
                if r.isChecked():
                    x_param = self.x_radios.get(r)

            for r in self.y_radios:
                if r.isChecked():
                    y_param = self.y_radios.get(r)

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
