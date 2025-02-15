"""
@file custom_types.py

@desc File for keeping custom types of JSONConfig Library

@author Rushil Shah
@email rushils4@illinois.edu | shahrushil520@gmail.com
"""

from typing import TypeAlias

InterpretedConfigFile : TypeAlias = dict[str, "InterpretedConfigFile"] | list["InterpretedConfigFile"] | str | int | float | bool | None