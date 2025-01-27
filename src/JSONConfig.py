"""
@file JSONConfig.py
@author Rushil Shah
@maintainer Rushil Shah
@email rushils4@illinois.edu | shahrushil520@gmail.com

@desc Class to interpret JSON files as configs
"""

# Data Collection Libraries
import os
import json
import csv
import h5py
import numpy as np
from PIL import Image
from shutil import copy

from typing import List, Union

class JSONConfig:

    path_to_json : str
    json_data : dict
    gray_cameras : dict
    semantic_cameras : dict
    iteration_number : int
    imu_available : bool
    imu_data_types : List[str] = ["accelerometer_x", 
                                  "accelerometer_y", 
                                  "accelerometer_z", 
                                  "gyroscope_x", 
                                  "gyroscope_y", 
                                  "gyroscope_z"
                                  ]
    min_target_velocity : float
    max_target_velocity : float
    store_in_hdf5 : bool

    def __init__(self, path_to_json : str):

        self.path_to_json = path_to_json

        # Try to Open the file & Load JSON data as dictionary
        try:
            file = open(self.path_to_json)
            self.json_data = json.load(file)
        except PermissionError:
            print("You don't have permission to open the file.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            exit()

        # Safety Checks
        self.initial_safety_checks()
        
        # Initialize variables
        self.gray_cameras = self.json_data["available_gray_cameras"]
        self.semantic_cameras = self.json_data["available_semantic_cameras"]
        self.iteration_number = self.json_data["iteration"]
        self.imu_available = self.json_data["imu_available"]
        self.min_target_velocity = self.json_data["min_drive_velocity"]
        self.max_target_velocity = self.json_data["max_drive_velocity"]
        self.store_in_hdf5 = self.json_data["store_in_hdf5"]
    
    def initial_safety_checks(self) -> None:
        # Check for Essential Configurations
        necessary_configs = ["iteration", 
                             "available_gray_cameras", 
                             "available_semantic_cameras", 
                             "imu_available", 
                             "min_drive_velocity", "max_drive_velocity",
                             "store_in_hdf5"]
        print(self.json_data["iteration"])
        for i in necessary_configs:
            try: print(self.json_data[i])
            except KeyError as ke:
                print("This key does not exist in the file. You have provided an invalid file.", end="")
                print(f" Add key {ke}")

        # Confirm if directories are safe
        user_safe_directories_query : bool = \
            True \
            if input("Is it safe to proceed? Have you checked all directories?") == "Y" \
            else False
        
        if user_safe_directories_query: return
        else: exit()
