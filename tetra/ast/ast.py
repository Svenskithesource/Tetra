"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

import typing, tokens

class AST:
    """The main class which all nodes will inherit from.
    """
    pass

class IntegerLiteral(AST):
    def __init__(self, value: int):
        self.value = value

class Add(AST):
    def __init__(self, left: IntegerLiteral, right: IntegerLiteral):
        self.left = left
        self.right = right

class Sub(AST):
    def __init__(self, left: IntegerLiteral, right: IntegerLiteral):
        self.left = left
        self.right = right

class Module(AST):
    def __init__(self, name: str, body: typing.List):
        self.name = name
        self.body = body
    
class Parser:
    def __init__(self, tokens: typing.Generator):
        self.tokens = tokens
        self.cur_token = tokens.next()
    
    def error(self, msg: str):
        raise SyntaxError(msg)