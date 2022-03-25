"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from enum import Enum, auto

class Token(Enum):
    """All tokens in the language."""
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    MUL = auto()
    DIV = auto()
    LPARAN = auto()
    RPARAN = auto()
    NAME = auto()
    EQUAL = auto()
    NEWLINE = auto()
    STRING = auto()
    LBRACE = auto()
    RBRACE = auto()
    EOF = auto()

class TokenInfo:
    """Represents a token in the source code.
    """
    def __init__(self, token_type: Token, value, line: str,lineo: int, column: int):
        self.token_type = token_type
        self.value = value
        self.column = column
        self.line = line
        self.lineo = lineo
    
    def __str__(self):
        return f"TokenInfo(token_type={self.token_type}, value={self.value}, line={self.line}, column={self.column})"

    def __repr__(self):
        return str(self)

    def __getitem__(self, key): # so you can e.g. do token[0] or token["token_type"]
        if isinstance(key, str):
            return self.__dict__[key]
        elif isinstance(key, int):
            return list(self.__dict__.values())[key]
        else:
            raise KeyError("Invalid key type")
        