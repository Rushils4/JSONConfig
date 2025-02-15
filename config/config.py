"""
@file config.py
@author Rushil Shah
@maintainer Rushil Shah
@email rushils4@illinois.edu | shahrushil520@gmail.com

@desc File holding central config class
"""

from config_exceptions import *
import file_interpret
import custom_types

class Config:

    path_to_config_file : str
    deserialized_configs : list[custom_types.InterpretedConfigFile]
    extension : str
    config_names : list[str]

    def __init__(self, path_to_config_file : str) -> list[str]:

        if path_to_config_file == None or path_to_config_file == "":
            raise NoConfigProvided()
        
        self.path_to_config_file = path_to_config_file
        
        # Determine Type of File (JSON, YAML, XML)
        period_split_file_name : list[str] = path_to_config_file.split(".")

        # Interpret Provided Config File
        self.interpret_file(period_split_file_name[-1])
        
        return self.config_names
    
    def interpret_file(self, extension : str) -> None:
        if extension.lower() == "json":
            self.extension = extension
            config_names, deserialized_configs = self.__interpret_json(self.path_to_config_file)
            self.config_names = config_names
            self.serialized_config = deserialized_configs
        elif extension.lower() == "yaml":
            self.extension = extension
            config_names, deserialized_configs = self.__interpret_yaml(self.path_to_config_file)
            self.config_names = config_names
            self.serialized_config = deserialized_configs
        elif extension.lower() == "xml":
            self.extension = extension
            config_names, deserialized_configs = self.__interpret_xml(self.path_to_config_file)
            self.config_names = config_names
            self.serialized_config = deserialized_configs
        else:
            raise FileTypeNotCompatible()

    def __interpret_json(self, path_to_config_file) -> tuple[str, list[custom_types.InterpretedConfigFile]]:
        config_name, deserialized_config = file_interpret.interpret_json(path_to_config_file)
        return config_name, deserialized_config

    def __interpret_yaml(self, path_to_config_file) -> tuple[str, str]:
        config_name, deserialized_config = file_interpret.interpret_yaml(path_to_config_file)
        return config_name, deserialized_config

    def __interpret_xml(self, path_to_config_file) -> tuple[str, str]:
        config_name, deserialized_config = file_interpret.interpret_xml(path_to_config_file)
        return config_name, deserialized_config