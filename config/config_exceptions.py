"""
@file config_exceptions.py
@author Rushil Shah
@maintainer Rushil Shah
@email rushils4@illinois.edu | shahrushil520@gmail.com

@desc File holding exceptions for central config class.
"""

def BaseConfigException(Exception):
    """
    @brief Exception used as the base of any exception for the Config class.
    """
    def __init__(self):
        print("An error has occurred from Config: ", end="")

def InvalidConfig(BaseConfigException):
    """
    @brief Exception used as base for other more detailed exceptions where the config is invalid.
    """
    def __init__(self):
        super.__init__()
        print("The configuration is invalid: ", end="")

    def __str__(self):
        self.__init__(self)

def NoneConfig(InvalidConfig):
    """
    @brief Exception for when the config is None. Used when Config class is None or when the actual configuration variable None.
    """
    def __init__(self):
        super.__init__()
        print("There is no config.")

    def __str__(self):
        self.__init__(self)
    
def NoConfigProvided(InvalidConfig):
    """
    @brief Exception for when no config file was provided to the config class. Not used in any other scenario.
    """
    def __init__(self):
        super.__init__()
        print("No config file was provided.")
    
    def __str__(self):
        self.__init__(self)

def KeyNotFound(InvalidConfig):
    """
    @brief Exception for when a key isn't found in the config.
    """
    def __init__(self):
        super.__init__()
        print("Key not found.")
    
    def __init__(self, key : str):
        super.__init__()
        print(f"Key not found: {key}")

    def __str__(self):
        self.__init__(self)

    def __str__(self, key : str):
        self.__init__(self, key)

def InvalidPath(BaseConfigException):
    """
    @brief Exception used as base for other more detailed exceptions where a provided path is invalid.
    """
    def __init__(self):
        super.__init__()
        print("The file path is invalid: ", end="")

    def __str__(self):
        self.__init__(self)

def FileTypeNotCompatible(InvalidPath):
    """
    @brief Exception for when the provided path has an invalid extension.
    """
    def __init__(self, extension : str):
        super.__init__()
        print(f"Provided file has an unexpected/incompatible extension: {extension}")
    
    def __str__(self):
        self.__init__(self)

def ImpossiblePath(InvalidPath):
    """
    @brief Exception for when the provided file path literally cannot exist (uses invalid characters, etc.)
    """
    def __init__(self):
        super.__init__()
        print("Provided path can't possibly exist.")