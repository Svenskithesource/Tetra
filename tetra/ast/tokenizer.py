from enum import Enum, auto

class Token(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()

class TokenInfo:
    def __init__(self, token_type: Token, value, line: int, column: int):
        self.token_type = token_type
        self.value = value
        self.column = column
        self.line = line
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return self.__dict__[key]
        elif isinstance(key, int):
            return list(self.__dict__.values())[key]
        else:
            raise KeyError("Invalid key type")
        
