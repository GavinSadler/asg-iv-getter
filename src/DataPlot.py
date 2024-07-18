from typing import List, Optional

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

    smu_1_name: Optional[str]
    smu_2_name: Optional[str]

    datasets: List[Dataset]

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.datasets = []
        self.curves = []

        self.smu_1_name = None
        self.smu_2_name = None

        self.plot_item = self.addPlot(0, 0)
        self.plot_item.getAxis("left").enableAutoSIPrefix(True)
        self.plot_item.getAxis("bottom").enableAutoSIPrefix(True)
        self.plot_item.getAxis("top").enableAutoSIPrefix(True)
        self.plot_item.getAxis("right").enableAutoSIPrefix(True)

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

        # Use the provided SMU names for labels
        if self.x_param == PlotParam.time:
            x_label = "Time"
        if self.x_param in [PlotParam.smu_1_voltage, PlotParam.smu_1_current]:
            x_label = f"{self.smu_1_name}" if self.smu_1_name else "SMU 1"
        else:
            x_label = f"{self.smu_2_name}" if self.smu_2_name else "SMU 2"

        if self.y_param == PlotParam.time:
            y_label = "Time"
        if self.y_param in [PlotParam.smu_1_voltage, PlotParam.smu_1_current]:
            y_label = f"{self.smu_1_name}" if self.smu_1_name else "SMU 1"
        else:
            y_label = f"{self.smu_2_name}" if self.smu_2_name else "SMU 2"

        # Determine what unit to show on the graph axis
        if self.x_param == PlotParam.time:
            x_unit = "s"
        elif self.x_param in [PlotParam.smu_1_voltage, PlotParam.smu_2_voltage]:
            x_unit = "V"
        else:
            y_unit = "A"

        if self.y_param == PlotParam.time:
            y_unit = "s"
        elif self.y_param in [PlotParam.smu_1_voltage, PlotParam.smu_2_voltage]:
            y_unit = "V"
        else:
            y_unit = "A"

        self.plot_item.setLabel(axis="bottom", text=x_label, units=x_unit)
        self.plot_item.setLabel(axis="left", text=y_label, units=y_unit)

        self.refresh_all()

    def update_labels(self, smu_1_name: str, smu_2_name: str):
        self.smu_1_name = smu_1_name
        self.smu_2_name = smu_2_name

        self.set_plot_parameters(self.x_param, self.y_param)

    def show_plot_params_dialog(self):
        new_params = PlotParamsDialog(self, self.x_param, self.y_param, self.smu_1_name, self.smu_2_name).get_params()

        if new_params:
            self.set_plot_parameters(*new_params)
