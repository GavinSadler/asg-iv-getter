from dataclasses import dataclass
from enum import Enum


class MeasurementField(Enum):
    SMU_1_VOLTAGE = 0
    SMU_1_CURRENT = 1
    SMU_2_VOLTAGE = 2
    SMU_2_CURRENT = 3
    TIME = 4


@dataclass
class Measurement:
    smu_1_voltage: float
    smu_1_current: float
    smu_2_voltage: float
    smu_2_current: float
    time: float
