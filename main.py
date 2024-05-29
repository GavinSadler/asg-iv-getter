import sys

from PySide6.QtWidgets import QApplication

from Controller import Controller

# Create the application instance
app = QApplication(sys.argv)

controller = Controller()
controller.smu_search_clicked()

# Enter the main event loop
sys.exit(app.exec())
