"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from enum import Enum, auto

class Opcode(Enum):
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    LOAD_CONST = auto()
    STORE_VAR = auto()
    LOAD_VAR = auto()
    JUMP_IF_FALSE = auto()
    JUMP_IF_TRUE = auto()
    RETURN = auto()
    DUMP = auto()

