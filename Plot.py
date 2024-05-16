import sys
import numpy as np
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
import matplotlib.pyplot as plt

class Plot(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._figure, self._axes = plt.subplots()
        self._canvas = FigureCanvasQTAgg(self._figure)

        layout = QVBoxLayout(self)
        layout.addWidget(NavigationToolbar2QT(self._canvas))
        layout.addWidget(self._canvas)

        self._line, = self._axes.plot([], [])
        self._x_data = np.array([])
        self._y_data = np.array([])

        self._legend_labels = []
        self._x_title = ""
        self._y_title = ""

    def update_plot(self, x_data: np.ndarray, y_data: np.ndarray):
        self._x_data = x_data
        self._y_data = y_data

        self._line.set_data(self._x_data, self._y_data)
        self._axes.relim()
        self._axes.autoscale_view()
        self._canvas.draw()

    def set_axis_titles(self, x_title: str, y_title: str):
        self._x_title = x_title
        self._y_title = y_title
        self._axes.set_xlabel(self._x_title)
        self._axes.set_ylabel(self._y_title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Plot()
    widget.set_axis_titles("X-axis", "Y-axis")
    
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