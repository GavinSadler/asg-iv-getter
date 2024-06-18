
import math
from typing import List
import pyqtgraph as pg

from Data import Dataset
from PlotParamsDialog import PlotParam, PlotParamsDialog

class DataPlot(pg.GraphicsLayoutWidget):
    
    plot_item: pg.PlotItem
    legend: pg.LegendItem

    x_param: PlotParam
    y_param: PlotParam
    
    datasets: List[Dataset]
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.datasets = []
        
        self.plot_item = self.addPlot(0, 0)

        self.legend = pg.LegendItem(brush="Black")
        self.legend.setParentItem(self.plot_item.graphicsItem())
        self.legend.anchor(itemPos=(1, 0), parentPos=(1, 0), offset=(-10, 10))

        self.set_plot_parameters(PlotParam.smu_1_voltage, PlotParam.smu_1_current)
    
    def refresh(self):
        
        self.plot_item.clear()
        self.legend.clear()
        
        for d in self.datasets:
            p = self.plot_item.plot(pen=d.color)
            self.legend.addItem(p, f"{d.metadata.wafer_number} {d.metadata.chip_number} {d.metadata.step_of_process}")
            p.setData(d.data[self.x_param.name], d.data[self.y_param.name])
            
    def reset(self):
        self.datasets = []
        self.refresh()
    
    def set_plot_parameters(self, x_param: PlotParam, y_param: PlotParam):
        self.x_param = x_param
        self.y_param = y_param
        
        self.plot_item.setLabel(axis="bottom", text=x_param.name)
        self.plot_item.setLabel(axis="left", text=y_param.name)
        
        self.refresh()

    def show_plot_params_dialog(self):
        new_params = PlotParamsDialog(self, self.x_param, self.y_param).get_params()
        
        if new_params:
            self.set_plot_parameters(*new_params)