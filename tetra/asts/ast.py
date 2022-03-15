"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

import typing

from tetra.asts.tokenizer import TokenStream
from .tokens import *

class AST:
    """The main class which all nodes will inherit from."""
    def __str__(self): # To print the AST
        lines = [self.__class__.__name__ + ':']
        for key, val in vars(self).items():
            lines += '{}: {}'.format(key, val).split('\n')
        return '\n    '.join(lines)
    
    def __repr__(self): # For when it's in a list or similar
        return str(self)

class Store(AST):
    def __init__(self, index, value):
        self.index = index
        self.value = value

class Load(AST):
    def __init__(self, index):
        self.index = index

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
    def __init__(self, name: str, body: typing.List, constants: typing.List, vars: typing.List[str]):
        self.name = name
        self.body = body
        self.constants = constants
        self.vars = vars
    
class Parser:
    """The ast parser. All expressions are notated in the code descriptions are in the Backus-Naur form"""
    def __init__(self, tokens: TokenStream):
        self.constants = []
        self.vars = []
        self.tokens = tokens
        self.cur_token = self.tokens.next()
    
    def error(self, msg: str):
        raise SyntaxError(msg)
    
    def eat(self, token_type: Token):
        """Goes to the next token if the current token matches the given type"""
        if self.cur_token.token_type == token_type:
            self.cur_token = self.tokens.next()
        else:
            self.error("Expected {}".format(token_type))

    def factor(self):
        """factor ::= INTEGER | LPAREN expr RPAREN | VAR EQUAL expr"""
        if self.cur_token.token_type == Token.NUMBER:
            if int(self.cur_token.value) not in self.constants:
                self.constants.append(int(self.cur_token.value))
            
            node = IntegerLiteral(self.constants.index(int(self.cur_token.value)), int(self.cur_token.value))
            self.eat(Token.NUMBER)
            return node
        elif self.cur_token.token_type == Token.LPARAN:
            self.eat(Token.LPARAN)
            node = self.expr()
            self.eat(Token.RPARAN)
            return node
        elif self.cur_token.token_type == Token.NAME:
            value = self.cur_token.value

            self.eat(Token.NAME)
            if self.cur_token.token_type == Token.EQUAL:
                if not value in self.vars:
                    self.vars.append(value)
                self.eat(Token.EQUAL)
                node = Store(self.vars.index(value), self.expr())
                return node
            elif self.cur_token.token_type == Token.NEWLINE:
                try:
                    self.eat(Token.NEWLINE)
                    return Load(self.vars.index(value))
                except ValueError:
                    self.error(f"Variable '{value}' undefined")
            else:
                self.error("Expected '=' or a newline")

        else:
            self.error(f"Expected INTEGER or ( or NAME, got {self.cur_token.token_type}")
        

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
        nodes = [self.expr()]
        while self.cur_token.token_type == Token.NEWLINE:
            self.eat(Token.NEWLINE)
            if self.cur_token.token_type == Token.EOF:
                break
            nodes.append(self.expr())
        return Module("test", nodes, self.constants, self.vars)
    