import random
from enum import Enum
from typing import List

import serial
import serial.serialutil
import serial.tools.list_ports
from PySide6.QtCore import QObject, QThread, Signal, Slot


class Source(Enum):
    VOLTAGE = 0
    CURRENT = 1


class Mode(Enum):
    SWEEP = 0
    CONSTANT = 1

def zero():
    return 0

# Comment this and the source meter will generate random garbage
# random.random = zero

def encode_float(f: float):
    """Turns a float value into bytes"""
    return f"{f:.6f}".encode()

class SourceMeter:

    simulated: bool
    serial_number: str
    source_mode: Source
    _conn: serial.Serial

    def __init__(self, device: serial.Serial = None):

        # Chekc if our device is simulated (No valid serial object was passed to the class)
        self.simulated = device is None
        self._conn = device

        if self.simulated:
            self.serial_number = "SIMULATED"

        # Just initialize the supply to supply voltage, initially
        self.reset()
        self.initialize_supply(Source.VOLTAGE, 0.01)

    def reset(self):
        """Resets the SMU"""
        if not self.simulated:
            # Turn off the SMU output
            self._send_command(b":OUTP OFF")
            # Reset the SMU to defaults
            self._send_command(b"*RST")
            # Return only voltage and current measurements back to us
            self._send_command(b":FORM:ELEM VOLT,CURR")

    def disconnect(self):
        if not self.simulated:
            self.reset()
            self._conn.close()

    def initialize_supply(self, supply_source: Source, compliance: float):
        """Sets the SMU supply source and sense parameters, with specified compliance"""
                
        if supply_source is Source.VOLTAGE:
            self._send_command(b":SOUR:FUNC VOLT")
            self._send_command(b":SENS:CURR:PROT:LEV " + encode_float(compliance))
        else:
            self._send_command(b":SOUR:FUNC CURR")
            self._send_command(b":SENS:VOLT:PROT:LEV " + encode_float(compliance))
            
        self.source_mode = supply_source

    def source(self, supply_value: float):
        """Sources the provided source_value, to the specified output source"""
        if self.source_mode is Source.VOLTAGE:
            self._send_command(b":SOUR:VOLT:LEV:IMM:AMPL " + encode_float(supply_value))
        else:
            self._send_command(b":SOUR:CURR:LEV:IMM:AMPL " + encode_float(supply_value))

    def measure(self):
        """Obtains a measurement from the SMU, as (voltage: float, current: float)"""

        # Flush the input buffer of the serial device before the next measurement
        self._flush_input_buffer()

        if self.source_mode is Source.VOLTAGE:
            self._send_command(b":MEAS:CURR?")
        else:
            self._send_command(b":MEAS:VOLT?")

        if not self.simulated:
            voltage_str, current_str = self._read_input_buffer().decode().strip().split(",")
            return (float(voltage_str), float(current_str))
        else:
            return (random.random(), random.random())

    def beep(self, frequency: int, time: float):
        self._send_command(f":SYST:BEEP:IMM {frequency}, {time}".encode())

    def output_off(self):
        """Disables SMU power output"""
        self._send_command(b":OUTP OFF")

    def _send_command(self, command: bytes, ending: bytes = b"\n"):
        """Sends a command to the serial device, if not in simulation mode."""
        if not self.simulated and self._conn:

            self._conn.write(command)

            if ending != b"":
                self._conn.write(ending)

    def _flush_input_buffer(self):
        """Reads everything in the serial input buffer, if not in simulation mode."""
        if not self.simulated and self._conn:
            return self._conn.read_all()

    def _read_input_buffer(self):
        """Waits for and reads the next line of the serial input buffer, if not in simulation mode."""
        if not self.simulated and self._conn:
            return self._conn.read_until()


class ConnectSMUWorker(QThread):

    progress_update = Signal(int)
    status_update = Signal(str)
    connections_made = Signal(list)

    _cancel_search: bool
    _timeout: int

    def __init__(self, parent: QObject = None, timeout: int = 1):
        super().__init__(parent)
        self._cancel_search = False
        self._timeout = timeout

    def run(self):

        smu_connections: List[SourceMeter] = []

        ports = serial.tools.list_ports.comports()

        self.progress_update.emit(0)
        self.status_update.emit("Scanning ports for SMUs...")

        # Iterate through all serial port devices
        for i, port in enumerate(ports):

            if self._cancel_search:
                break

            self.progress_update.emit(int(100 * i / len(ports)))
            self.status_update.emit(f"-----")
            self.status_update.emit(f"Trying to connect to port '{port.name}'")

            try:
                device = serial.Serial(port.name, timeout=self._timeout, write_timeout=self._timeout)
            except serial.SerialException:
                self.status_update.emit(f"Could not connect to port '{port.name}'")
                continue

            self.status_update.emit(f"Connected to port '{port.name}'")

            try:
                # Flush and read the identity
                device.read_all()
                device.write(b"*IDN?\n")
                identity = device.read_until()
            except serial.SerialTimeoutException:
                self.status_update.emit(f"Port '{port.name}' timed out when asked for identification")
                continue

            self.status_update.emit(f"Port '{port.name}' gave the following identification: {identity}")

            # Verify the device is a Keithley device, and
            if b"KEITHLEY INSTRUMENTS INC." in identity:
                sm = SourceMeter(device)
                sm.serial_number = identity.split(b",")[2].decode()
                smu_connections.append(sm)
                self.status_update.emit(f"Port '{port.name}' successfully identified as a valid SMU")

        self.progress_update.emit(100)
        self.status_update.emit(f"-----")
        self.status_update.emit(f"Port scan concluded\n")
        self.status_update.emit(f"Connected SMUs:")
        
        for connection in smu_connections:
            self.status_update.emit(f"{connection._conn.name}, SN:{connection.serial_number}")

        # Only return connections if the search was not cancelled
        if not self._cancel_search:
            self.connections_made.emit(smu_connections)
        else:
            self.status_update.emit(f"Search cancelled")
        
        # Add a newline after the search is finished
        self.status_update.emit("")

    @Slot()
    def cancel_search(self):
        self._cancel_search = True


if __name__ == "__main__":

    import sys

    from PySide6.QtCore import QCoreApplication

    app = QCoreApplication(sys.argv)

    connect_smus = ConnectSMUWorker(timeout=3)

    connect_smus.progress_update.connect(lambda x: print(f"Progress: {x}%"))
    connect_smus.status_update.connect(lambda x: print(x))

    def print_connections(connections: List[SourceMeter]):
        for connection in connections:
            print(f"Port: {connection._conn.name}\tSN: {connection.serial_number}")

    connect_smus.connections_made.connect(print_connections)
    connect_smus.finished.connect(app.quit)
    connect_smus.start()

    # Enter the main event loop
    sys.exit(app.exec())
