import time
from dataclasses import dataclass
from enum import Enum

import numpy as np
from PySide6.QtCore import QThread, Signal, Slot

from Data import MeasurementPoint
from SourceMeter import Source, SourceMeter


def sleep(seconds: float):
    """Wrapper around QThread.usleep, gives best sleep accuracy"""
    QThread.usleep(int(seconds * 1000000))


@dataclass
class SweepParameters:
    sweep_source: Source
    sweep_start: float
    sweep_step: float
    sweep_end: float
    sweep_compliance: float

    constant_source: Source
    constant_start: float
    constant_step: float
    constant_end: float
    constant_compliance: float

    pause_between_measurements: float
    pause_between_sweeps: float
    test_count: int
    repeat_sweep: bool


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

def list_values(start: float, stop: float, step: float):
    step = abs(step)
    
    if start == stop:
        return np.array([start])
    
    if start <= stop:
        return np.arange(start, stop + step, step)
    else:
        return np.arange(start, stop - step, -step)

class SweepMeasurementWorker(QThread):

    measurement_made = Signal(MeasurementPoint)

    sweep_begin = Signal(float)
    sweep_complete = Signal()
    
    # test_began = Signal()
    # test_complete = Signal()

    # constant_supply_now: float

    _parameters: SweepParameters
    _sweep_smu: SourceMeter
    _constant_smu: SourceMeter

    _sweep_supply_values: np.ndarray
    _constant_supply_values: np.ndarray

    _stop: bool

    def __init__(self, parameters: SweepParameters, sweep_smu: SourceMeter, constant_smu: SourceMeter):
        super().__init__()

        self._stop = False

        self._parameters = parameters
        self._sweep_smu = sweep_smu
        self._constant_smu = constant_smu

        # Precalculate the values that will be supplied to the SMUs
        self._sweep_supply_values = list_values(self._parameters.sweep_start, self._parameters.sweep_end, self._parameters.sweep_step)
        self._constant_supply_values = list_values(self._parameters.constant_start, self._parameters.constant_end, self._parameters.constant_step)

        # These variables can be used externally to track what the current constant supply is at
        self.constant_supply_now = self._constant_supply_values[0]

    def run(self):

        # Get the SMUs ready
        self._sweep_smu.initialize_supply(self._parameters.sweep_source, self._parameters.sweep_compliance)
        self._constant_smu.initialize_supply(self._parameters.constant_source, self._parameters.constant_compliance)

        if self._parameters.repeat_sweep:
            self.repeat_sweep()
        else:
            self.sweep_then_step()

        # Make sure to turn off SMUs after measurement
        self._sweep_smu.output_off()
        self._constant_smu.output_off()

    def sweep_then_step(self):
        
        for _ in range(self._parameters.test_count):

            for constant_output in self._constant_supply_values:
                
                # Set the constant SMU's supply value
                self._constant_smu.source(constant_output)
                
                self.sweep(constant_output)
                    
                if self._stop:
                    return

                sleep(self._parameters.pause_between_sweeps)
    
    def repeat_sweep(self):
        
        for constant_output in self._constant_supply_values:
            
            # Set the constant SMU's supply value
            self._constant_smu.source(constant_output)
            
            for _ in range(self._parameters.test_count):
                self.sweep(constant_output)
                
            if self._stop:
                return

            sleep(self._parameters.pause_between_sweeps)

    def sweep(self, constant_output: float):

        start_time = time.time()
        
        self.sweep_begin.emit(constant_output)

        for sweep_output in self._sweep_supply_values:

            if self._stop:
                return

            # Set the value for the sweep SMU
            self._sweep_smu.source(sweep_output)

            # Sleep a bit before taking the first measurement
            sleep(self._parameters.pause_between_measurements)

            # Take our measuremnt
            sv, sc = self._sweep_smu.measure()
            cv, cc = self._constant_smu.measure()
            t = time.time() - start_time

            mp = MeasurementPoint(sv, sc, cv, cc, t)

            # Notify subscribers
            self.measurement_made.emit(mp)

        self.sweep_complete.emit()

    @Slot()
    def stop(self):
        self._stop = True


if __name__ == "__main__":

    import sys
    from typing import List

    from PySide6.QtCore import QCoreApplication, QTimer

    from SourceMeter import ConnectSMUWorker

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
