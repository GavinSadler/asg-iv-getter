import sys

from matplotlib import pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from PySide6.QtWidgets import QApplication, QDoubleSpinBox, QMainWindow

from ui_main_window import Ui_MainWindow


class UserInterface(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Make sure the SMU parameters change when 
        self.ui.smu_1_mode.currentTextChanged.connect(lambda: self.update_smu_parameters(1))
        self.ui.smu_1_supply.currentTextChanged.connect(lambda: self.update_smu_parameters(1))
        self.ui.smu_2_mode.currentTextChanged.connect(lambda: self.update_smu_parameters(2))
        self.ui.smu_2_supply.currentTextChanged.connect(lambda: self.update_smu_parameters(2))
        self.update_smu_parameters(1)
        self.update_smu_parameters(2)

        # Create a Matplotlib figure and axis
        self.figure, self.axis = plt.subplots()

        # Create a FigureCanvas object and pass the Matplotlib figure to it
        self.canvas = FigureCanvasQTAgg(self.figure)
        
        self.ui.graph_container.addWidget(NavigationToolbar2QT(self.canvas))
        self.ui.graph_container.addWidget(self.canvas)

        # Plot a sine wave on the Matplotlib figure
        self.plot_sine_wave()

    def plot_sine_wave(self):
        # Generate x values
        x = np.linspace(0, 2 * np.pi, 100)

        # Generate y values (sine wave)
        y = np.sin(x)

        # Plot the sine wave on the Matplotlib figure
        self.axis.plot(x, y)

        # Refresh the canvas
        self.canvas.draw()

    def update_smu_parameters(self, smu_number: int):

        if not isinstance(smu_number, int):
            raise TypeError("Parameter 'smu_number' must be of type int")

        supply = getattr(self.ui, f"smu_{smu_number}_supply").currentText()
        mode = getattr(self.ui, f"smu_{smu_number}_mode").currentText()

        if mode == "Sweep":
            disable_sweep = False
        elif mode == "Constant":
            disable_sweep = True

        if supply == "Voltage":
            measure = "Current"
        elif supply == "Current":
            measure = "Voltage"

        if smu_number != 1 and smu_number != 2:
            raise ValueError(f"Only two SMUs can be connected, either SMU 1 or SMU 2. Parameter smu_number was {smu_number}")

        # Update the labels
        getattr(self.ui, f"sweep_start_label_{smu_number}").setText(f"{supply} Start")
        getattr(self.ui, f"sweep_step_label_{smu_number}").setText(f"{supply} Step")
        getattr(self.ui, f"sweep_end_label_{smu_number}").setText(f"{supply} End")
        getattr(self.ui, f"supply_label_{smu_number}").setText(f"{supply} Supply")
        getattr(self.ui, f"compliance_label_{smu_number}").setText(f"{measure} Compliance")

        # Update the inputs
        set_input_type(getattr(self.ui, f"sweep_start_{smu_number}"), supply)
        set_input_type(getattr(self.ui, f"sweep_step_{smu_number}"), supply)
        set_input_type(getattr(self.ui, f"sweep_end_{smu_number}"), supply)
        set_input_type(getattr(self.ui, f"supply_{smu_number}"), supply)
        set_input_type(getattr(self.ui, f"compliance_{smu_number}"), measure)

        # Disable either constant or sweep option

        getattr(self.ui, f"supply_label_{smu_number}").setDisabled(not disable_sweep)
        getattr(self.ui, f"supply_{smu_number}").setDisabled(not disable_sweep)

        getattr(self.ui, f"sweep_start_label_{smu_number}").setDisabled(disable_sweep)
        getattr(self.ui, f"sweep_step_label_{smu_number}").setDisabled(disable_sweep)
        getattr(self.ui, f"sweep_end_label_{smu_number}").setDisabled(disable_sweep)
        getattr(self.ui, f"sweep_start_{smu_number}").setDisabled(disable_sweep)
        getattr(self.ui, f"sweep_step_{smu_number}").setDisabled(disable_sweep)
        getattr(self.ui, f"sweep_end_{smu_number}").setDisabled(disable_sweep)


def set_input_type(input: QDoubleSpinBox, unit: str):
    if unit == "Voltage":
        input.setSuffix(" V")
        input.setMinimum(-1100)
        input.setMaximum(1100)
    elif unit == "Current":
        input.setSuffix(" A")
        input.setMinimum(-5)
        input.setMaximum(5)


if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window
    ui = UserInterface()

    # Display the QLabel widget
    ui.show()

    # Enter the main event loop
    sys.exit(app.exec())
