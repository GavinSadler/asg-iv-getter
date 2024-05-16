from datetime import datetime
import os
import pandas as pd

from Measurement import MeasurementPoint

class Data:

    data: pd.DataFrame

    def __init__(self, file_path: str):
 
        # Store the file name
        self.file_path = file_path
        
        # Check if the file already exists, we don't want to overwrite preexisting data
        # if os.path.isfile(self.file_path):
        #     raise FileExistsError(f"{self.file_path} already exists")
        
        # Create an empty DataFrame
        self.data = pd.DataFrame(columns=['voltage_1', 'current_1', 'voltage_2', 'current_2', 'time'])
        
        # Set data types for each column
        for column in self.data.columns:
            self.data[column] = self.data[column].astype(float)

        with open(self.file_path, "w") as fp:
            #TODO: Figure out best way to print header information
            # Also make sure correct header information is printed
            fp.write(f"# {datetime.now()}\n")
            fp.write(f"# smu_1_serial: ?\tsmu_2_serial: ?\n")
            fp.write(f"# sweep_supply: ?\tsweep_start: ?\tsweep_step:\tsweep_end:?\tsweep_compliance: ?\n")
            fp.write(f"# constant_supply: ?\tconstant_output: ?\n")
            fp.write(f"# Wafer information: ?\n")
            fp.write("voltage_1,current_1,voltage_2,current_2,time\n")

    # def add_data(self, p: MeasurementPoint):
    #     self.add_data(p.sweep_voltage, p.sweep_current, p.constant_voltage, p.constant_current, p.time)

    def add_data(self, voltage_1: float, current_1: float, voltage_2: float, current_2: float, time: float):
        self.data = pd.concat(
            (self.data, pd.DataFrame({"voltage_1": [voltage_1], "current_1": [current_1], "voltage_2": [voltage_2], "current_2": [current_2], "time": [time]}))
        )

        # Write the updated DataFrame to the file
        with open(self.file_path, "a") as fp:
            fp.write(f"{voltage_1},{voltage_2},{current_1},{current_2},{time}\n")

if __name__ == "__main__":
    
    x = Data("test.csv")
    
    x.add_data(1, 2, 3, 4, 5)
    x.add_data(1, 2, 3, 4, 5)
    