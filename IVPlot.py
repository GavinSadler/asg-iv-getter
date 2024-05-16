from typing import List

import matplotlib
import matplotlib.axes
import matplotlib.lines
import matplotlib.figure
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import (FigureCanvasQTAgg,
                                               NavigationToolbar2QT)
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QVBoxLayout, QWidget

from Measurement import MeasurementPoint


class IVPlot(QWidget):
    
    _axes: List[matplotlib.axes.Axes]
    _lines: List[matplotlib.lines.Line2D]
    _figure: matplotlib.figure.Figure
    _canvas: FigureCanvasQTAgg
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self._data = []
        self._lines = []

        # Create a Matplotlib figure and axis
        self._figure, self._axes = plt.subplots(4)
            
        # Create a FigureCanvas object and pass the Matplotlib figure to it
        self._canvas = FigureCanvasQTAgg(self._figure)

        graph_container = QVBoxLayout(self)
        graph_container.addWidget(NavigationToolbar2QT(self._canvas))
        graph_container.addWidget(self._canvas)

        for a in self._axes:
            a.autoscale(True)
            self._lines.append(a.plot([0])[0])
        
    @Slot(pd.DataFrame)
    def update_plot(self, data: pd.DataFrame):
        
        self._lines[0].set_data(data['time'], data['voltage_1'])
        self._lines[1].set_data(data['time'], data['current_1'])
        self._lines[2].set_data(data['time'], data['voltage_2'])
        self._lines[3].set_data(data['time'], data['current_2'])
        
        for a in self._axes:
            a.relim()
            a.autoscale_view()
            
        # Refresh the canvas
        self._canvas.draw()