import pandas as pd
import pyqtgraph as pg

import Data
from PlotParamsDialog import PlotParam
from PySide6.QtGui import QColor
import math

class RealtimePlot(pg.GraphicsLayoutWidget):

    plot_item: pg.PlotItem
    legend: pg.LegendItem

    x_param: PlotParam
    y_param: PlotParam

    data: pd.DataFrame
    
    last_hue: float

    def __init__(self, parent=None, x_param=PlotParam.smu_1_voltage, y_param=PlotParam.smu_1_current, show_legend=True):
        super().__init__(parent=parent)

        self.last_hue = 0.0

        self.plot_item = self.addPlot(0, 0)
        
        self.legend = pg.LegendItem(brush="Black")
        self.legend.setParentItem(self.plot_item.graphicsItem())
        self.legend.anchor(itemPos=(1,0), parentPos=(1,0), offset=(-10,10))
        
        if not show_legend:
            self.legend.hide()
            
        self.reset()
        self.set_plot_parameters(x_param, y_param)

        self.data = Data.initialize_data()
        

    def reset(self):
        self.plot_item.clear()
        self.legend.clear()
        self.start_new_curve()

    def start_new_curve(self):
        # Rotate the hue value by pi/1.2
        # This ensures we generally get colors that contrast well
        self.last_hue += math.pi / 1.2
        
        if self.last_hue >= math.pi * 2:
            self.last_hue -= math.pi * 2
            
        p = self.plot_item.plot(pen=QColor.fromHsv(360 * self.last_hue / 2 / math.pi, 255, 255))
        self.legend.addItem(p, f"Run {len(self.legend.items)}")

    def set_plot_parameters(self, x_param: PlotParam, y_param: PlotParam):
        self.x_param = x_param
        self.y_param = y_param
        self.plot_item.setLabel(axis="bottom", text=x_param.name)
        self.plot_item.setLabel(axis="left", text=y_param.name)

    def update_data(self, data: pd.DataFrame):
        self.data = data
        curve: pg.PlotDataItem = self.plot_item.curves[-1]
        curve.setData(data[self.x_param.name], data[self.y_param.name])

if __name__ == "__main__":

    import random
    import sys
    import time

    from PySide6.QtWidgets import QApplication

    # Create the application instance
    app = QApplication(sys.argv)

    widget = RealtimePlot()

    # phase_shift = 0

    # def update_data():
    #     global phase_shift
    #     phase_shift += 0.1
    #     x_data = np.linspace(0, 10, 100) + phase_shift
    #     y_data = np.sin(x_data)
    #     widget.update_plot(x_data, y_data)

    # timer = QTimer()
    # timer.timeout.connect(update_data)
    # timer.timeout.connect(lambda: timer.start(0.1))
    # timer.start(0.1)

    d = Data.initialize_data()

    for i in range(100):
        d = pd.concat(
            (
                d,
                pd.DataFrame(
                    {
                        "smu_1_voltage": [random.random()],
                        "smu_1_current": [random.random()],
                        "smu_2_voltage": [random.random()],
                        "smu_2_current": [random.random()],
                        "time": [time.time()],
                    }
                ),
            )
        )
        time.sleep(0.01)

    widget.update_data(d)

    widget.show()

    # Enter the main event loop
    sys.exit(app.exec())
