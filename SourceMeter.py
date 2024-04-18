import time
from typing import List

import numpy as np
import serial
import serial.tools.list_ports


class SourceMeter:

    simulated: bool
    _conn: serial.Serial

    def __init__(self, device: serial.Serial = None):

        # Chekc if our device is simulated (No valid serial object was passed to the class)
        self.simulated = device is None
        self._conn = device

        self.reset()

    def reset(self):
        """Resets the SMU"""

        if not self.simulated:

            # Reset the SMU to defaults
            self._conn.write(b"*RST")
            # Return only voltage and current measurements back to us
            self._conn.write(b":FORM:ELEM VOLT,CURR")
            # Sets the SMU to measure DC current (I think?)
            self._conn.write(b":CONF:CURR:DC")
            # Limit current output to whatever compliance is set at
            # self._conn.write(b":SENS:CURR:PROT:LEV " + str(compliance).encode())
            # Tell the SMU to source voltage
            self._conn.write(b":SOUR:FUNC:MODE VOLT")
            # Turn off SMU output
            self._conn.write(b":OUTP OFF")

    def run_single_measurement(self, voltage_start: float, voltage_step: float, voltage_end: float, current_compliance: float, delay: float):
        """Runs a single measurement with the given parameters"""

        voltages = np.linspace(voltage_start, voltage_end, int(abs((voltage_end - voltage_start) / voltage_step)) + 1)
        currents = np.zeros_like(voltages)

        self.enable_source_voltage(current_compliance)

        for i, v in enumerate(voltages):
            currents[i] = self.measure_current(v, delay)

        self.output_off()

        return (voltages, currents)

    def run_measurements(self, num_measurements: int, voltage_start: float, voltage_step: float, voltage_end: float, compliance: float, delay: float):

        measurement_results = []

        for _ in range(num_measurements):
            measurement_results.append(self.run_single_measurement(voltage_start, voltage_step, voltage_end, compliance, delay))

        return np.array(measurement_results)

    def enable_source_voltage(self, current_compliance: float):
        """Sets the SMU to source voltage and sense current, with specified current compliance"""
        if not self.simulated:
            self._send_command(b":SOUR:FUNC VOLT")
            self._send_command(b":SENS:CURR:PROT:LEV " + str(current_compliance).encode())

    def enable_source_current(self, voltage_compliance: float):
        """Sets the SMU to source current and sense voltage, with specified voltage compliance"""
        if not self.simulated:
            self._send_command(b":SOUR:FUNC CURR")
            self._send_command(b":SENS:VOLT:PROT:LEV " + str(voltage_compliance).encode())

    def measure_current(self, voltage: float, delay: float):
        """Measures the current for the supplied voltage, after a given delay"""

        if not self.simulated:
            self._send_command(b":SOUR:VOLT:LEV:IMM:AMPL " + str(voltage).encode())

            time.sleep(delay)

            # Flush the input buffer of the serial device before the next measurement
            self._read_input_buffer()

            self._send_command(b":MEAS:CURR?")

            return float(self._read_input_buffer().decode())

        else:
            time.sleep(delay)
            return np.random.rand()

    def measure_voltage(self, current: float, delay: float):
        """Measures the voltage for the supplied current, after a given delay"""

        if not self.simulated:
            self._send_command(b":SOUR:CURR:LEV:IMM:AMPL " + str(current).encode())

            time.sleep(delay)

            # Flush the input buffer of the serial device before the next measurement
            self._read_input_buffer()

            self._send_command(b":MEAS:VOLT?")

            return float(self._read_input_buffer().decode())
        else:
            time.sleep(delay)
            return np.random.rand()

    def output_off(self):
        """Disables SMU power output"""
        self._send_command(b":OUTP OFF")

    def _send_command(self, command: bytes):
        """Sends a command to the serial device, if not in simulation mode."""
        if not self.simulated and self._conn:
            self._conn.write(command)

    def _read_input_buffer(self):
        """Reads the serial input buffer, if not in simulation mode."""
        if not self.simulated and self._conn:
            return self._conn.read_all()


def identify_smus():

    smu_connections: List[serial.Serial] = []

    # Iterate through all serial port devices
    for port in serial.tools.list_ports.comports():

        try:
            device = serial.Serial(port)
        except serial.SerialException:
            # We couldn't connect to the device, move onto the next one
            continue

        # Ask the device for its identity
        if b"KEITHLEY INSTRUMENTS INC.,MODEL 2400,1212298,C30   Mar 17 2006 09:29:29/A02  /K/J" in query(device, b"*IDN?"):
            smu_connections.append(device)

    # Return all connected SMUs
    return smu_connections
