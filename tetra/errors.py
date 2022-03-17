"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

class Error:
    def __init__(self, type: str, name: str, message: str, line: str, lineo: int, col: int, repl: bool = False):
        self.type = type
        self.name = name
        self.message = message
        self.line = line
        self.lineo = lineo
        self.col = col
        self.repl = repl

    def raise_exception(self):
        print()
        print(f"In {self.name} on line {self.lineo}")
        if not self.repl:
            print(f"{self.line}")
            print(f"{' ' * (self.col)}^")
        print(f"{self.type}: {self.message}")

def error(*args, **kwargs):
    Error(*args, **kwargs).raise_exception()
    if (len(args) == 7 and not args[6]): # TODO: Find a better way to check if it's running in repl mode
        exit()