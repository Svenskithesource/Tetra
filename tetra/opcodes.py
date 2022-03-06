"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from enum import Enum, auto

class Opcode(Enum):
    ADD = auto()
    SUB = auto()
    LOAD_CONST = auto()
    DUMP = auto()

