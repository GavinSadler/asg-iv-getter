from typing import List

import pyqtgraph as pg

from Data import Dataset
from PlotParamsDialog import PlotParam, PlotParamsDialog

pg.setConfigOptions(antialias=True, background="w", foreground="k")


class DataPlot(pg.GraphicsLayoutWidget):

    plot_item: pg.PlotItem
    curves: List[pg.PlotDataItem]
    legend: pg.LegendItem

    x_param: PlotParam
    y_param: PlotParam

    datasets: List[Dataset]

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.datasets = []
        self.curves = []

        self.plot_item = self.addPlot(0, 0)

        self.legend = pg.LegendItem()
        self.legend.setBrush(pg.mkBrush(255, 255, 255, int(0.9 * 255)))
        self.legend.setParentItem(self.plot_item.graphicsItem())
        self.legend.anchor(itemPos=(1, 0), parentPos=(1, 0), offset=(-10, 10))

        self.set_plot_parameters(PlotParam.smu_1_voltage, PlotParam.smu_1_current)

    def add_dataset(self, data: Dataset):
        self.datasets.append(data)
        p = self.plot_item.plot(pen=data.color)

        self.legend.addItem(p, data.get_label())

        x_data = getattr(data, self.x_param.name)
        y_data = getattr(data, self.y_param.name)

        p.setData(x_data, y_data)

        self.curves.append(p)

    def remove_last_dataset(self):
        self.datasets.pop()

        c = self.curves.pop()
        self.legend.removeItem(c)
        c.clear()

    def refresh_all(self):
        # Create a datasets reference
        datasets_reference = self.datasets
        self.datasets = []

        # Clear all of the plot elements
        self.plot_item.clear()
        self.legend.clear()

        # Go through and re-add all of the datasets
        for d in datasets_reference:
            self.add_dataset(d)

    def refresh_latest(self):
        x_data = getattr(self.datasets[-1], self.x_param.name)
        y_data = getattr(self.datasets[-1], self.y_param.name)

        self.curves[-1].setData(x_data, y_data)

    def reset(self):
        self.datasets.clear()
        self.curves.clear()

        self.refresh_all()

    def set_plot_parameters(self, x_param: PlotParam, y_param: PlotParam):
        self.x_param = x_param
        self.y_param = y_param

        self.plot_item.setLabel(axis="bottom", text=x_param.name)
        self.plot_item.setLabel(axis="left", text=y_param.name)

        self.refresh_all()

    def show_plot_params_dialog(self):
        new_params = PlotParamsDialog(self, self.x_param, self.y_param).get_params()

        if new_params:
            self.set_plot_parameters(*new_params)
