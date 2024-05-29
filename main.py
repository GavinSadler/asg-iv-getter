import sys

from PySide6.QtWidgets import QApplication

from Controller import Controller
from MainWindow import MainWindow

if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)

    # The controller handles the rest
    controller = Controller()
    
    # Enter the main event loop
    sys.exit(app.exec())
