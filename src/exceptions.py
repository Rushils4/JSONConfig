"""
@file exceptions.py
@author Rushil Shah
@maintainer Rushil Shah
@email rushils4@illinois.edu | shahrushil520@gmail.com

@desc File to create custom exceptions for the JSONConfig class
"""

import JSONConfig as jsc

def BaseJSONConfigException(Exception):
    
    def __init__(self):
        print("An error has occurred from JSONConfig: ", end="")

def InvalidConfig(BaseJSONConfigException):

    def __init__(self):
        super.__init__()
        print("The configuration is invalid: ", end="")

    def __str__(self):
        self.__init__(self)

def NoneConfig(InvalidConfig):
    
    def __init__(self):
        super.__init__()
        print("There is no config.")

    def __str__(self):
        self.__init__(self)

def NoConfigProvided(InvalidConfig):

    def __init__(self):
        super.__init__()
        print("No config file was provided.")