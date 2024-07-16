from typing import Dict, List, Optional

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from SMUNameDialog import SMUNameDialog
from SourceMeter import ConnectSMUWorker, SourceMeter
from UserInterface.ui_smu_search_dialog import Ui_smu_search_dialog


class SMUSearchDialog(QtWidgets.QDialog, Ui_smu_search_dialog):

    connections: List[SourceMeter]
    sourcemeter_names: Dict[str, str]

    def __init__(
        self,
        existing_connections: Optional[List[SourceMeter]] = None,
        sourcemeter_names: Optional[Dict[str, str]] = None,
        parent: Optional[QtWidgets.QWidget] = None,
    ):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.connections = existing_connections or []
        self.sourcemeter_names = sourcemeter_names or {}

        self.search.clicked.connect(self.search_clicked)
        self.connection_list.itemSelectionChanged.connect(self.connection_selection_changed)

        self.smu_disconnect.clicked.connect(self.disconnect_clicked)
        self.smu_identify.clicked.connect(self.identify_clicked)
        self.smu_name.clicked.connect(self.name_clicked)

        self.search.clicked.connect(self.search_clicked)

        self.update_list()

    def get_sourcemeters(self):
        self.exec()
        return self.connections

    @QtCore.Slot()
    def search_clicked(self):
        # Disconnect all currently connected SMUs
        self.disconnect_all_smus()

        # Create the search thread
        self._smu_search_thread = ConnectSMUWorker(self)
        self._smu_search_thread.progress_update.connect(self.search_progress.setValue)
        self._smu_search_thread.status_update.connect(self.search_log.appendPlainText)
        self._smu_search_thread.connections_made.connect(self.connect_smus)
        self._smu_search_thread.finished.connect(self.smu_search_finished)

        # Update the search button
        self.search.setText("Cancel SMU Search")
        self.search.clicked.disconnect()
        self.search.clicked.connect(self._smu_search_thread.cancel_search)

        # Disable the connections list
        self.smu_connections.setDisabled(True)

        # Start the search
        self._smu_search_thread.start()

    @QtCore.Slot()
    def smu_search_finished(self):
        # Update the search button
        self.search.setText("Search for SMUs")
        self.search.clicked.disconnect()
        self.search.clicked.connect(self.search_clicked)

        # Enable the connections list
        self.smu_connections.setDisabled(False)

        # Reset the progress bar
        self.search_progress.reset()

    def update_list(self):
        # Clear and re-add SMUs to the list
        self.connection_list.clear()

        for smu in self.connections:

            if smu.name:
                label = f"{smu.name} ({smu.serial_number})"
            else:
                label = smu.serial_number

            self.connection_list.addItem(label)

    @QtCore.Slot()
    def disconnect_all_smus(self):
        # Make sure to gracefully disconnect SMUs
        for smu in self.connections:
            smu.disconnect()

        self.connections = []

        self.update_list()

    @QtCore.Slot()
    def connect_smus(self, smus: List[SourceMeter]):
        # Disconnect any SMUs that may be connected
        self.disconnect_all_smus()
        self.connections = smus

        # If the sourcemeter has been given a name, make sure to apply it here
        for smu in self.connections:
            if smu.serial_number in self.sourcemeter_names.keys():
                smu.name = self.sourcemeter_names[smu.serial_number]

        self.update_list()

    def get_smu_from_serial(self, serial: str):
        for smu in self.connections:
            if smu.serial_number == serial:
                return smu

    def get_selected_smu(self):
        if len(self.connection_list.selectedItems()) == 0:
            return None

        text = self.connection_list.selectedItems()[0].text()

        # In the case that there is a paren in the text, there should be an associated name
        if "(" in text:
            serial = text.split("(")[1][:-1]
        else:
            # Otherwise, the text is the serial
            serial = text

        return self.get_smu_from_serial(serial)

    @QtCore.Slot()
    def connection_selection_changed(self):
        smu = self.get_selected_smu()

        self.smu_disconnect.setDisabled(smu is None)
        self.smu_identify.setDisabled(smu is None)
        self.smu_name.setDisabled(smu is None)

    @QtCore.Slot()
    def disconnect_clicked(self):
        smu = self.get_selected_smu()

        if smu:
            smu.disconnect()
            self.connections.remove(smu)
            self.update_list()

    @QtCore.Slot()
    def identify_clicked(self):
        smu = self.get_selected_smu()

        if smu:
            smu.identify()

    @QtCore.Slot()
    def name_clicked(self):
        smu = self.get_selected_smu()

        smu.name = SMUNameDialog(smu.name, self).get_name()

        self.update_list()


if __name__ == "__main__":

    import sys

    # Create the application instance
    app = QtWidgets.QApplication(sys.argv)

    ui = SMUSearchDialog()
    ui.show()

    # Enter the main event loop
    sys.exit(app.exec())
