import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

from PlotParamsDialog import PlotParam, PlotParamsDialog


class Plot(QWidget):

    data: pd.DataFrame
    x_plot: PlotParam
    y_plot: PlotParam

    _figure: Figure
    _axes: Axes
    _line: Line2D
    _canvas: FigureCanvasQTAgg

    def __init__(self, data: pd.DataFrame, parent=None):
        super().__init__(parent)

        # Initialize fields
        self.data = data

        self._figure, self._axes = plt.subplots()
        self._canvas = FigureCanvasQTAgg(self._figure)

        layout = QVBoxLayout(self)
        # layout.addWidget(NavigationToolbar2QT(self._canvas))
        layout.addWidget(self._canvas)

        (self._line,) = self._axes.plot([], [])

        # Update titles
        self.update_plot_params(PlotParam.smu_1_voltage, PlotParam.smu_1_current)
        
        self._line.set_data(self.data[self.x_plot.name], self.data[self.y_plot.name])
        
        self.refresh()

    @Slot()
    def show_plot_params_dialog(self):
        new_params = PlotParamsDialog(pd.DataFrame(columns=PlotParam.strings()), self, self.x_plot, self.y_plot).get_params()
        if new_params:
            x, y = new_params
            self.update_plot_params(x, y)

    @Slot()
    def update_plot_params(self, x: PlotParam, y: PlotParam):
        self.x_plot = x
        self.y_plot = y
        self._axes.set_xlabel(self.x_plot.name)
        self._axes.set_ylabel(self.y_plot.name)
        self.refresh()
        self.update_data(self.data)

    @Slot()
    def refresh(self):
        self._figure.tight_layout()
        self._axes.autoscale_view()
        self._axes.relim()
        self._canvas.draw()

    @Slot()
    def update_data(self, new_data: pd.DataFrame):
        self.data = new_data
        self._line.set_data(self.data[self.x_plot.name], self.data[self.y_plot.name])
        self._axes.set_xlabel(self.x_plot.name)
        self._axes.set_ylabel(self.y_plot.name)
        self._figure.tight_layout()
        self._axes.autoscale_view()
        self._axes.relim()
        self._canvas.draw()
    
    @Slot()
    def start_new_plot(self):
        (self._line,) = self._axes.plot([], [])
    
    @Slot()
    def reset(self):
        self._axes.clear()
        self.start_new_plot()
        self.refresh()
    
    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     self.refresh()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Plot()
    widget.set_titles("X-axis", "Y-axis")

    phase_shift = 0

    def update_data():
        global phase_shift
        phase_shift += 0.1
        x_data = np.linspace(0, 10, 100) + phase_shift
        y_data = np.sin(x_data)
        widget.update_plot(x_data, y_data)

    timer = QTimer()
    timer.timeout.connect(update_data)
    timer.timeout.connect(lambda: timer.start(0.1))
    timer.start(0.1)

    widget.show()
    sys.exit(app.exec())
