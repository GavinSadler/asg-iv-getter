from dataclasses import dataclass
from enum import Enum
import time

import numpy as np
from PySide6.QtCore import QThread, Signal, Slot

from SourceMeter import Source, SourceMeter


def sleep(seconds: float):
    """Wrapper around QThread.usleep, gives best sleep accuracy"""
    QThread.usleep(int(seconds * 1000000))


@dataclass
class MeasurementPoint:
    smu_1_voltage: float
    smu_1_current: float
    smu_2_voltage: float
    smu_2_current: float
    time: float


@dataclass
class SweepParameters:
    sweep_source: Source
    sweep_start: float
    sweep_step: float
    sweep_end: float
    sweep_compliance: float

    constant_source: Source
    constant_output: float
    constant_compliance: float

    measurement_pause: float
    sweep_pause: float
    sweep_count: int


class DatastreamMode(Enum):
    CONTINUOUS = 0
    FIXED_COUNT = 1
    FIXED_DURATION = 2


@dataclass
class DatastreamParameters:
    smu_1_source: Source
    smu_1_output: float
    smu_1_compliance: float

    smu_2_source: Source
    smu_2_output: float
    smu_2_compliance: float

    measurement_mode: DatastreamMode
    measurement_pause: float
    measurement_duration: float
    measurement_count: int


class DatastreamMeasurementWorker(QThread):

    parameters: DatastreamParameters
    smu_1: SourceMeter
    smu_2: SourceMeter

    measurement_made = Signal(MeasurementPoint)

    _stop: bool

    def __init__(self, parameters: DatastreamParameters, smu_1: SourceMeter, smu_2: SourceMeter):
        super().__init__()

        self._stop = False

        self.parameters = parameters
        self.smu_1 = smu_1
        self.smu_2 = smu_2

    def run(self):

        iterations = 0
        start_time = time.time()

        # Get the SMUs ready
        self.smu_1.initialize_supply(self.parameters.smu_1_source, self.parameters.smu_1_compliance)
        self.smu_2.initialize_supply(self.parameters.smu_2_source, self.parameters.smu_2_compliance)

        # Set the SMUs to output their respective values
        self.smu_1.source(self.parameters.smu_1_output)
        self.smu_2.source(self.parameters.smu_2_output)

        # Sleep a bit before taking the first measurement
        sleep(self.parameters.measurement_pause)

        while not self._stop:

            # Take our measuremnt
            s1v, s1c = self.smu_1.measure()
            s2v, s2c = self.smu_2.measure()
            t = time.time() - start_time

            mp = MeasurementPoint(s1v, s1c, s2v, s2c, t)

            # And notify subscribers
            self.measurement_made.emit(mp)

            # Break the loop if we were instructed to stop after a given parameter
            iterations += 1
            if (
                (self.parameters.measurement_mode is DatastreamMode.FIXED_COUNT and iterations >= self.parameters.measurement_count)
                or (self.parameters.measurement_mode is DatastreamMode.FIXED_DURATION and time.time() - start_time > self.parameters.measurement_duration)
                or self._stop
            ):
                break

            sleep(self.parameters.measurement_pause)

        # Make sure to turn off SMUs after measurement
        self.smu_1.output_off()
        self.smu_2.output_off()

    @Slot()
    def stop(self):
        self._stop = True


class SweepMeasurementWorker(QThread):

    parameters: SweepParameters
    sweep_smu: SourceMeter
    constant_smu: SourceMeter

    measurement_made = Signal(MeasurementPoint)
    sweep_complete = Signal()

    _stop: bool

    def __init__(self, parameters: SweepParameters, sweep_smu: SourceMeter, constant_smu: SourceMeter):
        super().__init__()

        self._stop = False

        self.parameters = parameters
        self.sweep_smu = sweep_smu
        self.constant_smu = constant_smu

    def run(self):

        num_sweeps = 0

        while not self._stop:

            self.sweep()
            self.sweep_complete.emit()

            num_sweeps += 1
            if num_sweeps >= self.parameters.sweep_count or self._stop:
                break

            sleep(self.parameters.sweep_pause)

        # Make sure to turn off SMUs after measurement
        self.sweep_smu.output_off()
        self.constant_smu.output_off()

    def sweep(self):

        start_time = time.time()
        supply_values = np.arange(self.parameters.sweep_start, self.parameters.sweep_end + self.parameters.sweep_step, self.parameters.sweep_step)
        i = 0

        # Get the SMUs ready
        self.sweep_smu.initialize_supply(self.parameters.sweep_source, self.parameters.sweep_compliance)
        self.constant_smu.initialize_supply(self.parameters.constant_source, self.parameters.constant_compliance)

        # Set the SMUs to output their respective values
        self.sweep_smu.source(supply_values[i])
        self.constant_smu.source(self.parameters.constant_output)

        # Sleep a bit before taking the first measurement
        sleep(self.parameters.measurement_pause)

        while not self._stop:

            # Take our measuremnt
            sv, sc = self.sweep_smu.measure()
            cv, cc = self.constant_smu.measure()
            t = time.time() - start_time

            mp = MeasurementPoint(sv, sc, cv, cc, t)

            # Notify subscribers
            self.measurement_made.emit(mp)

            # Check to see if we've gone through all of the supplied values
            i += 1
            if i >= len(supply_values) or self._stop:
                break

            # Output new value at sweep
            self.sweep_smu.source(supply_values[i])

            sleep(self.parameters.measurement_pause)

        # After we finish the sweep, turn off the SMUs
        self.sweep_smu.output_off()
        self.constant_smu.output_off()

    @Slot()
    def stop(self):
        self._stop = True


if __name__ == "__main__":

    import sys

    from PySide6.QtCore import QCoreApplication, QTimer

    from SourceMeter import ConnectSMUWorker
    from typing import List

    app = QCoreApplication(sys.argv)

    connect_smus = ConnectSMUWorker()

    connect_smus.progress_update.connect(lambda x: print(f"Progress: {x}%"))
    connect_smus.status_update.connect(print)

    def print_connections(connections: List[SourceMeter]):
        for connection in connections:
            print(f"Port: {connection._conn.name}\tSN: {connection.serial_number}")

    def take_measurements(connections: List[SourceMeter]):

        if len(connections) == 0:
            connections.append(SourceMeter())
            connections.append(SourceMeter())
        elif len(connections) == 1:
            connections.append(SourceMeter())

        print("=== Testing Datastream count ===")

        dsp = DatastreamParameters(Source.CURRENT, 0.010, 10, Source.VOLTAGE, 10, 0.020, DatastreamMode.FIXED_COUNT, 0.1, -1, 10)
        dsw = DatastreamMeasurementWorker(dsp, connections[0], connections[1])
        dsw.measurement_made.connect(print)
        dsw.finished.connect(lambda: print("Count finished"))
        dsw.finished.connect(dsw.deleteLater)

        dsw.start()
        dsw.wait()

        print("=== Testing Datastream time ===")

        dsp = DatastreamParameters(Source.CURRENT, 0.010, 10, Source.VOLTAGE, 10, 0.020, DatastreamMode.FIXED_DURATION, 0.1, 5, -1)
        dsw = DatastreamMeasurementWorker(dsp, connections[0], connections[1])
        dsw.measurement_made.connect(print)
        dsw.finished.connect(lambda: print("Time finished"))
        dsw.finished.connect(dsw.deleteLater)

        dsw.start()
        dsw.wait()

        print("=== Testing Datastream continuous ===")

        dsp = DatastreamParameters(Source.CURRENT, 0.010, 10, Source.VOLTAGE, 10, 0.020, DatastreamMode.FIXED_DURATION, 0.1, 5, -1)
        dsw = DatastreamMeasurementWorker(dsp, connections[0], connections[1])
        dsw.measurement_made.connect(print)
        dsw.finished.connect(lambda: print("Continuous was cut off"))
        dsw.finished.connect(dsw.deleteLater)

        timer = QTimer()
        timer.timeout.connect(dsw.stop)

        dsw.start()
        timer.start(1000 * 3.5)
        dsw.wait()

        print("=== Testing Sweep ===")

        sp = SweepParameters(Source.VOLTAGE, -1.5, 0.1, 1.5, 0.010, Source.CURRENT, 0.010, 10, 0.01, 1, 3)
        sw = SweepMeasurementWorker(sp, connections[0], connections[1])
        sw.measurement_made.connect(print)
        sw.sweep_complete.connect(lambda: print("Sweep completed"))
        sw.finished.connect(lambda: print("Sweeps finished"))
        sw.finished.connect(sw.deleteLater)

        sw.start()
        sw.wait()

        print("=== Testing Sweep, but we cut it off ===")

        sp = SweepParameters(Source.VOLTAGE, -1.5, 0.1, 1.5, 0.010, Source.CURRENT, 0.010, 10, 0.01, 1, 3)
        sw = SweepMeasurementWorker(sp, connections[0], connections[1])
        sw.measurement_made.connect(print)
        sw.sweep_complete.connect(lambda: print("Sweep completed"))
        sw.finished.connect(lambda: print("Sweeps cut off"))
        sw.finished.connect(sw.deleteLater)

        timer = QTimer()
        timer.timeout.connect(sw.stop)

        sw.start()
        timer.start(1000 * 3.5)
        sw.wait()

        print("End")
        app.quit()

    connect_smus.connections_made.connect(print_connections)
    connect_smus.connections_made.connect(take_measurements)
    connect_smus.finished.connect(connect_smus.deleteLater)
    connect_smus.start()

    # Enter the main event loop
    sys.exit(app.exec())
