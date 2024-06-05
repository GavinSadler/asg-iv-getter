from PySide6.QtWidgets import QMainWindow

from Plot import Plot
from PlotParamsDialog import PlotParam
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)

    def setup_plots(self, ms_data, ds_data):
        self.sm_plot_smu_1 = Plot(ms_data, self.sm_plot_container)
        self.sm_plot_smu_1.update_plot_params(PlotParam.smu_1_voltage, PlotParam.smu_1_current)
        self.sm_plot_container.layout().addWidget(self.sm_plot_smu_1)
        
        self.sm_plot_smu_2 = Plot(ms_data, self.sm_plot_container)
        self.sm_plot_smu_2.update_plot_params(PlotParam.smu_2_voltage, PlotParam.smu_2_current)
        self.sm_plot_container.layout().addWidget(self.sm_plot_smu_2)

        self.ds_plot_smu_1 = Plot(ds_data, self.ds_plot_container)
        self.ds_plot_smu_1.update_plot_params(PlotParam.time, PlotParam.smu_1_current)
        self.ds_plot_container.layout().addWidget(self.ds_plot_smu_1)
        
        self.ds_plot_smu_2 = Plot(ds_data, self.ds_plot_container)
        self.ds_plot_smu_2.update_plot_params(PlotParam.time, PlotParam.smu_2_current)
        self.ds_plot_container.layout().addWidget(self.ds_plot_smu_2)


if __name__ == "__main__":

    import sys

    from PySide6.QtWidgets import QApplication

    # Create the application instance
    app = QApplication(sys.argv)

    ui = MainWindow()
    ui.show()

    # Enter the main event loop
    sys.exit(app.exec())
