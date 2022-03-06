"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

import typing, tokens


class IntegerLiteral:
    def __init__(self, value: int):
        self.value = value

class Add:
    def __init__(self, left: IntegerLiteral, right: IntegerLiteral):
        self.left = left
        self.right = right

class Sub:
    def __init__(self, left: IntegerLiteral, right: IntegerLiteral):
        self.left = left
        self.right = right

class Module:
    def __init__(self, name: str, body: typing.List):
        self.name = name
        self.body = body
    

