"""
@file interpret_json.py

@desc File for JSON file interpretation

@author Rushil Shah
@email rushils4@illinois.edu | shahrushil520@gmail.com
"""

import custom_types
from config.config_exceptions import *

import json

def interpret_json(path_to_config_file : str) -> tuple[str, list[custom_types.InterpretedConfigFile]]:
    """
    @func interpret_json
    @desc Function to interpret a JSON file whose filepath is passed as an input.

    @param path_to_config_file : str | Relative file path to config file from working directory
    @output tuple[str, InterpretedConfigFile] | Tuple of config name and length-one dictionary with str keys & any possible subset of InterpretedConfigFile for recursive interpretation
    """

    # Sanitize Inputted Config Filepath
    if path_to_config_file == None or path_to_config_file == "":
        raise NoConfigProvided()

    # Open JSON File and Extract Content
    config_file : custom_types.InterpretedConfigFile
    try:
        json_file = open(path_to_config_file, 'r')
        config_file = json.load(json_file)
        json_file.close()
    except OSError:
        raise InvalidPath()
    except Exception as e:
        raise e

    # Extract Config Name
    try:
        config_name = config_file["config_name"]
    except KeyError:
        raise KeyNotFound("config_name")

    # Return Config Name & Deserialized Content
    return config_name, config_file

def interpret_json(path_to_config_file : str, levels : int) -> tuple[str, list[custom_types.InterpretedConfigFile]]:
    """
    @func interpret_json
    @desc Function to interpret a JSON file with multiple sub-configs whose filepath is passed as an input

    @param path_to_config_file : str | Relative file path to config file from working directory
    @param levels : int | Number of layers of sub-configs
    @output tuple[str, List[InterpretedConfigFile]] | Tuple of config name and list of dictionaries with str keys & any possible subset of InterpretedConfigFile for recursive interpretation
    """

    # Sanitize Inputted Levels
    if (levels <= 0):
        print("Invalid Number of Levels Provided\nLevels Use: levels : int > 0")

    # Sanitize Inputted Config Filepath


    # Open JSON File and Extract Content


    # Break up Extracted Content into List of Dictionaries


    # Extract Configs Names


    # Return Config Name & Deserialized Content