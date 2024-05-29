from enum import Enum
from typing import List

import pandas as pd
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QGroupBox, QHBoxLayout, QRadioButton, QVBoxLayout

from ui_plot_params_dialog import Ui_Dialog


class PlotParam(Enum):
    smu_1_voltage = 0
    smu_1_current = 1
    smu_2_voltage = 2
    smu_2_current = 3
    time = 4
    
    def strings() -> List[str]:
        return [p.name for p in PlotParam]


# class PlotParamsDialog(QDialog, Ui_Dialog):

#     plot_params_updated = Signal(PlotParam, PlotParam)

#     def __init__(self, parent=None, x: PlotParam = PlotParam.smu_1_voltage, y: PlotParam = PlotParam.smu_1_current):
#         QDialog.__init__(self)
#         self.setupUi(self)
#         self.retranslateUi(self)

#         # Uncheck all boxes
#         c: QRadioButton
#         for c in self.findChildren(QRadioButton):
#             c.setChecked(False)

#         # Check the passed in x box
#         if x is PlotParam.smu_1_voltage:
#             self.x_smu_1_v.setChecked(True)
#         elif x is PlotParam.smu_2_voltage:
#             self.x_smu_2_v.setChecked(True)
#         elif x is PlotParam.smu_1_current:
#             self.x_smu_1_c.setChecked(True)
#         elif x is PlotParam.smu_2_current:
#             self.x_smu_2_c.setChecked(True)
#         elif x is PlotParam.time:
#             self.x_t.setChecked(True)

#         # Check the passed in y box
#         if y is PlotParam.smu_1_voltage:
#             self.y_smu_1_v.setChecked(True)
#         elif y is PlotParam.smu_2_voltage:
#             self.y_smu_2_v.setChecked(True)
#         elif y is PlotParam.smu_1_current:
#             self.y_smu_1_c.setChecked(True)
#         elif y is PlotParam.smu_2_current:
#             self.y_smu_2_c.setChecked(True)
#         elif y is PlotParam.time:
#             self.y_t.setChecked(True)

#         # Accept/reject signals
#         self.accepted.connect(self.on_accepted)

#     Slot()

#     def on_accepted(self):
#         # Identify which boxes are checked...
#         if self.x_smu_1_v.isChecked():
#             ppx = PlotParam.smu_1_voltage
#         elif self.x_smu_2_v.isChecked():
#             ppx = PlotParam.smu_2_voltage
#         elif self.x_smu_1_c.isChecked():
#             ppx = PlotParam.smu_1_current
#         elif self.x_smu_2_c.isChecked():
#             ppx = PlotParam.smu_2_current
#         elif self.x_t.isChecked():
#             ppx = PlotParam.time

#         if self.y_smu_1_v.isChecked():
#             ppy = PlotParam.smu_1_voltage
#         elif self.y_smu_2_v.isChecked():
#             ppy = PlotParam.smu_2_voltage
#         elif self.y_smu_1_c.isChecked():
#             ppy = PlotParam.smu_1_current
#         elif self.y_smu_2_c.isChecked():
#             ppy = PlotParam.smu_2_current
#         elif self.y_t.isChecked():
#             ppy = PlotParam.time

#         # And notify subscribers
#         self.plot_params_updated.emit(ppx, ppy)

class PlotParamsDialog(QDialog, Ui_Dialog):

    x_radios: List[QRadioButton]
    y_radios: List[QRadioButton]
    
    def __init__(self, df: pd.DataFrame, parent=None, x_selected: PlotParam = PlotParam.smu_1_voltage, y_selected: PlotParam = PlotParam.smu_1_current):
        QDialog.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        
        # Initialize fields
        self.x_radios: List[QRadioButton] = []
        self.y_radios: List[QRadioButton] = []
        
        # Add all of the radio buttons
        for column in df.columns:
            x_radio = QRadioButton(column, self.x_radio_group)
            self.x_radios.append(x_radio)
            self.x_radio_group.layout().addWidget(x_radio)

            if x_radio.text() == x_selected.name:
                x_radio.setChecked(True)

            y_radio = QRadioButton(column, self.y_radio_group)
            self.y_radios.append(y_radio)
            self.y_radio_group.layout().addWidget(y_radio)

            if y_radio.text() == y_selected.name:
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

    import pandas as pd
    from PySide6.QtWidgets import QApplication

    # Create the application instance
    app = QApplication(sys.argv)

    print(PlotParamsDialog(pd.DataFrame(columns=[p.name for p in PlotParam])).get_params())

    # Enter the main event loop
    sys.exit(app.exec())
