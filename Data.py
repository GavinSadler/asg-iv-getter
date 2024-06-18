import math
import os
from dataclasses import dataclass
from datetime import datetime
from PySide6.QtGui import QColor
import random

import pandas as pd


@dataclass
class Metadata:
    wafer_number: str
    chip_number: str
    step_of_process: str
    light_dark: str
    date: str
    time: str
    comments: str

    smu_1_serial: str = ""
    smu_2_serial: str = ""


@dataclass
class MeasurementPoint:
    smu_1_voltage: float
    smu_1_current: float
    smu_2_voltage: float
    smu_2_current: float
    time: float

class Dataset:
    data: pd.DataFrame
    metadata: Metadata
    color: QColor
    
    def initialize(metadata: dict = None):
        """Returns a Dataset with empty metadata"""
        if metadata is None:
            metadata = {}

        df = pd.DataFrame(columns=["smu_1_voltage", "smu_1_current", "smu_2_voltage", "smu_2_current", "time"])

        for column in df.columns:
            df[column] = df[column].astype(float)

        d = Dataset()
        d.data = df
        d.metadata = metadata
        d.color = QColor.fromHsv(360 * random.random(), 255, 255)

        return d

def write_data(output_file_path: str, data: Dataset, include_time=True):

    metadata = [
        data.metadata.wafer_number,
        data.metadata.chip_number,
        data.metadata.step_of_process,
        data.metadata.light_dark,
        data.metadata.date,
        data.metadata.time,
        data.metadata.comments,
    ]
    
    new_data = data.data

    # Write if no file exists, otherwise append to the existing file
    write_mode = "w" if not os.path.exists(output_file_path) else "a"

    if include_time:
        smu_1_data = new_data[["time", "smu_1_voltage", "smu_1_current"]]
        smu_2_data = new_data[["time", "smu_2_voltage", "smu_2_current"]]
    else:
        smu_1_data = new_data[["smu_1_voltage", "smu_1_current"]]
        smu_2_data = new_data[["smu_2_voltage", "smu_2_current"]]

    with pd.ExcelWriter(output_file_path, mode=write_mode, if_sheet_exists=("overlay" if write_mode == "a" else None), engine="openpyxl") as writer:

        if "SMU 1" in writer.book.sheetnames:
            # If we have an SMU 1 sheet, grab the next available column
            append_start_column_index = writer.book["SMU 1"].max_column + 1
        else:
            # If there is no SMU 1 sheet, then we are in a fresh file, start at column index 1
            append_start_column_index = 1

        # Depending on which columns are included on the written data, we need to perform a diffent floor division and write a different amount of metadata
        columns = len(smu_1_data.columns)

        # Add an _# depending on what run is being appended
        smu_1_data = smu_1_data.add_suffix(f"_{append_start_column_index // columns}")
        smu_2_data = smu_2_data.add_suffix(f"_{append_start_column_index // columns}")

        # For some reason, startcol in the below context starts at 0 rather than 1, like the rest of the excel libraries? Weird...
        smu_1_data.to_excel(writer, sheet_name="SMU 1", index=None, startrow=len(metadata), startcol=append_start_column_index - 1)
        smu_2_data.to_excel(writer, sheet_name="SMU 2", index=None, startrow=len(metadata), startcol=append_start_column_index - 1)

        # This will append the passed metadata information to the last set of columns of the data
        for column_num in range(append_start_column_index, append_start_column_index + columns):
            for row_num, value in enumerate(metadata, start=1):
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

        write_data(output_file_path, run_df, metadata, random.random() > 0.5)
