from typing import List

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

from SourceMeter import ConnectSMUWorker, SourceMeter
from UserInterface.ui_smu_search_dialog import Ui_smu_search_dialog


class SMUSearchDialog(QtWidgets.QDialog, Ui_smu_search_dialog):

    connections: List[SourceMeter]

    def __init__(self, existing_connections: List[SourceMeter] = []):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)

        self.connections = existing_connections

        self.search.clicked.connect(self.search_clicked)
        self.connection_list.itemSelectionChanged.connect(self.connection_selection_changed)
        self.smu_disconnect.clicked.connect(self.disconnect_clicked)
        self.smu_identify.clicked.connect(self.identify_clicked)

        self.search.clicked.connect(self.search_clicked)

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
            self.connection_list.addItem(smu.serial_number)

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

        self.update_list()

    def get_smu_from_serial(self, serial: str):
        for smu in self.connections:
            if smu.serial_number == serial:
                return smu

    def get_selected_smu(self):
        if len(self.connection_list.selectedItems()) == 0:
            return None

        serial = self.connection_list.selectedItems()[0].text()

        return self.get_smu_from_serial(serial)

    @QtCore.Slot()
    def connection_selection_changed(self):
        smu = self.get_selected_smu()

        self.smu_disconnect.setDisabled(smu is None)
        self.smu_identify.setDisabled(smu is None)

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
            smu.beep(1000, 0.5)


if __name__ == "__main__":

    import sys

    # Create the application instance
    app = QtWidgets.QApplication(sys.argv)

    ui = SMUSearchDialog()
    ui.show()

    # Enter the main event loop
    sys.exit(app.exec())
