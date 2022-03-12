"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

import typing
from .tokens import *

class AST:
    """The main class which all nodes will inherit from."""
    def __str__(self): # To print the AST
        lines = [self.__class__.__name__ + ':']
        for key, val in vars(self).items():
            lines += '{}: {}'.format(key, val).split('\n')
        return '\n    '.join(lines)

class IntegerLiteral(AST):
    def __init__(self, index, value: int):
        self.index = index
        self.value = value

class Add(AST):
    def __init__(self, left: IntegerLiteral, right: IntegerLiteral):
        self.left = left
        self.right = right

class Sub(AST):
    def __init__(self, left: IntegerLiteral, right: IntegerLiteral):
        self.left = left
        self.right = right

class Mul(AST):
    def __init__(self, left: IntegerLiteral, right: IntegerLiteral):
        self.left = left
        self.right = right

class Div(AST):
    def __init__(self, left: IntegerLiteral, right: IntegerLiteral):
        self.left = left
        self.right = right

class Module(AST):
    def __init__(self, name: str, body: typing.List, constants: typing.List):
        self.name = name
        self.body = body
        self.constants = constants
    
class Parser:
    """The ast parser. All expressions are notated in the code descriptions are in the Backus-Naur form"""
    def __init__(self, tokens: typing.Generator):
        self.constants = []
        self.tokens = tokens
        self.cur_token = tokens.next()
    
    def error(self, msg: str):
        raise SyntaxError(msg)
    
    def eat(self, token_type: Token):
        """Goes to the next token if the current token matches the given type"""
        if self.cur_token.token_type == token_type:
            self.cur_token = self.tokens.next()
        else:
            self.error("Expected {}".format(token_type))

    def factor(self):
        """factor ::= INTEGER"""
        
        if not self.cur_token.value in self.constants:
            self.constants.append(int(self.cur_token.value))
        node = IntegerLiteral(self.constants.index(int(self.cur_token.value)), int(self.cur_token.value))
        self.eat(Token.NUMBER)
        return node

    def term(self):
        """term ::= factor { ('*'|'/') factor }"""
        node = self.factor()
        while self.cur_token.token_type in (Token.MUL, Token.DIV):
            op = self.cur_token
            
            if op.token_type == Token.MUL:
                self.eat(Token.MUL)
                node = Mul(node, self.factor())
            elif op.token_type == Token.DIV:
                self.eat(Token.DIV)
                node = Div(node, self.factor())
            else:
                self.error("Unknown operator")

        return node

    def expr(self):
        """expr ::= term { ('+'|'-') term }"""
        node = self.term()
        while self.cur_token.token_type in (Token.PLUS, Token.MINUS):
            op = self.cur_token
            if op.token_type == Token.PLUS:
                self.eat(Token.PLUS)
                node = Add(node, self.term())
            elif op.token_type == Token.MINUS:
                self.eat(Token.MINUS)
                node = Sub(node, self.term())
            else:
                self.error("Unknown operator")
            
        return node
    
    def parse(self):
        return Module("test", self.expr(), self.constants)
    