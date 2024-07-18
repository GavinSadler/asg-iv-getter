import random
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

import pandas as pd
import PySide6.QtGui as QtGui


@dataclass
class MeasurementPoint:
    smu_1_voltage: float
    smu_1_current: float
    smu_2_voltage: float
    smu_2_current: float
    time: float


class Dataset:

    # Data fields
    smu_1_voltage: List[float]
    smu_1_current: List[float]
    smu_2_voltage: List[float]
    smu_2_current: List[float]
    time: List[float]

    # Should we write time to disk upon saving?
    write_time: bool

    # Metadata that gets printed out to the excel doc upon saving
    metadata: Dict[str, str]

    # The color of the line that will be used to show the data
    color: QtGui.QColor

    # Static variable used to determine the color of the next dataset
    _color_angle = 0.0

    def __init__(self, metadada: Dict[str, str] | None = None, write_time=True, increment_color_angle=True):

        if metadada:
            self.metadata = metadata.copy()
        else:
            self.metadata = {}

        self.smu_1_voltage = []
        self.smu_1_current = []
        self.smu_2_voltage = []
        self.smu_2_current = []
        self.time = []

        self.write_time = write_time

        self.color = QtGui.QColor.fromHsv(Dataset._color_angle, 255, 255)

        # We add this seemingly arbitrary angle as it is the Golden Angle
        # https://en.wikipedia.org/wiki/Golden_angle
        if increment_color_angle:
            Dataset._color_angle += 137.507

        # Make sure we don't go over 360 deg
        if Dataset._color_angle >= 360:
            Dataset._color_angle -= 360

    def get_label(self):

        label = f"{self.metadata.get("Wafer #")} {self.metadata.get("Comments")} {self.metadata.get("Constant Supply")}"

        return label

    def copy(self):
        d_new = Dataset(increment_color_angle=False)

        d_new.metadata = self.metadata.copy()

        d_new.smu_1_voltage = self.smu_1_voltage.copy()
        d_new.smu_1_current = self.smu_1_current.copy()
        d_new.smu_2_voltage = self.smu_2_voltage.copy()
        d_new.smu_2_current = self.smu_2_current.copy()
        d_new.time = self.time.copy()

        d_new.write_time = self.write_time

        d_new.color = QtGui.QColor(self.color)

        return d_new

    def write_to_excel(self, writer: pd.ExcelWriter):

        # If there is no SMU 1 sheet, then we are in a fresh file, start at column index 1
        append_start_column_index = 1

        # If we have an SMU 1 sheet, grab the next available column
        if "SMU 1" in writer.book.sheetnames:
            append_start_column_index = writer.book["SMU 1"].max_column + 1

        smu_1_data = {}
        smu_2_data = {}

        # If we include time data, 3 columns will be taken up by the data
        num_columns = 2
        if self.write_time:
            smu_1_data["time"] = self.time
            smu_2_data["time"] = self.time
            num_columns = 3

        smu_1_data["smu_1_voltage"] = self.smu_1_voltage
        smu_1_data["smu_1_current"] = self.smu_1_current

        smu_2_data["smu_2_voltage"] = self.smu_2_voltage
        smu_2_data["smu_2_current"] = self.smu_2_current

        # Create the dataframes, should be easier to print to excel when we do this
        smu_1_data = pd.DataFrame(smu_1_data).reset_index(drop=True)
        smu_2_data = pd.DataFrame(smu_2_data).reset_index(drop=True)

        # For some reason, startcol in the below context starts at 0 rather than 1, like the rest of the Excel
        # libraries? Weird...
        smu_1_data.to_excel(writer, sheet_name="SMU 1", index=False, startrow=len(self.metadata), startcol=append_start_column_index - 1)
        smu_2_data.to_excel(writer, sheet_name="SMU 2", index=False, startrow=len(self.metadata), startcol=append_start_column_index - 1)

        # This will append the passed metadata information to the last set of columns of the data
        for column_num in range(append_start_column_index, append_start_column_index + num_columns):
            for row_num, value in enumerate(self.metadata.values(), start=1):
                writer.book["SMU 1"].cell(row=row_num, column=column_num, value=f"{value}")
                writer.book["SMU 2"].cell(row=row_num, column=column_num, value=f"{value}")


if __name__ == "__main__":

    import random

    output_file_path = "output.xlsx"

    # Run 5-10 randomized runs
    for i in range(random.randint(5, 10)):

        metadata = {
            "Wafer #": random.randint(1, 10),
            "Chip #": random.randint(1, 10),
            "Step of Process": random.randint(1, 10),
            "Light/Dark": "Light" if random.random() > 0.5 else "Dark",
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Comments": "Hello!",
        }

        r = []

        for i in range(random.randint(20, 50)):
            r.append([i, random.random(), random.random(), random.random(), random.random()])

        run_df = pd.DataFrame(r, columns=["time", "smu_1_voltage", "smu_1_current", "smu_2_voltage", "smu_2_current"])

        # write_data(output_file_path, run_df, metadata, random.random() > 0.5)
