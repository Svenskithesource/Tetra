"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

import typing

from tetra.asts.tokenizer import TokenStream
from .tokens import *
from tetra.errors import error


class AST:
    """The main class which all nodes will inherit from."""

    def __str__(self):  # To print the AST
        lines = [self.__class__.__name__ + ':']
        for key, val in vars(self).items():
            lines += '{}: {}'.format(key, val).split('\n')
        return '\n    '.join(lines)

    def __repr__(self):  # For when it's in a list or similar
        return str(self)


class If(AST):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


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


class String(AST):
    def __init__(self, index, value: str):
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

    def __init__(self, name, tokens: TokenStream, repl):
        self.repl = repl
        self.name = name
        self.constants = []
        self.vars = []
        self.tokens = tokens
        self.cur_token = self.tokens.next()

    def eat(self, token_type: Token):
        """Goes to the next token if the current token matches the given type"""
        if self.cur_token.token_type == token_type:
            self.cur_token = self.tokens.next()
        else:
            error("SyntaxError", self.name, f"Expected {token_type}", self.cur_token.line, self.cur_token.lineo,
                  self.cur_token.column)

    def assign(self):
        """assign ::= VAR EQUAL expr"""
        value = self.cur_token.value

        if not value in self.vars:
            self.vars.append(value)
        self.eat(Token.NAME)
        self.eat(Token.EQUAL)
        if self.repl:
            node = Store(value,
                         self.expr())  # Store the var name if it's run in repl because we don't know if it's defined or not
        else:
            node = Store(self.vars.index(value), self.expr())

        return node

    def factor(self):
        """factor ::= INTEGER | STRING | LPAREN expr RPAREN | VAR"""
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
            try:
                if self.repl:
                    return Load(
                        value)  # Store the var name if it's run in repl because we don't know if it's defined or not
                else:
                    return Load(self.vars.index(value))
            except ValueError:
                error("NameError", self.name, f"Variable '{value}' undefined", self.tokens.peek_old().line,
                      self.tokens.peek_old().lineo, self.tokens.peek_old().column, self.repl)
        elif self.cur_token.token_type == Token.STRING:

            string = str(self.cur_token.value[1:-1])  # Remove the quotes
            if string not in self.constants:
                self.constants.append(string)
            self.eat(Token.STRING)
            return String(self.constants.index(string), string)
        else:
            error("SyntaxError", self.name, f"Expected INTEGER or ( or NAME, got {self.cur_token.token_type}",
                  self.cur_token.line, self.cur_token.lineo, self.cur_token.column, self.repl)

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
                error("SyntaxError", self.name, "Unknown operator", self.cur_token.line, self.cur_token.lineo,
                      self.cur_token.column, self.error)

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
                error("SyntaxError", self.name, "Unknown operator", self.cur_token.line, self.cur_token.lineo,
                      self.cur_token.column, self.error)

        return node

    def condition_statement(self):
        """condition_statement ::= "If" LPAREN expr RPAREN LBRACE program RBRACE"""
        self.eat(Token.NAME)
        self.eat(Token.LPARAN)

        condition = self.expr()

        self.eat(Token.RPARAN)
        self.eat(Token.LBRACE)

        body = self.program()

        self.eat(Token.RBRACE)
        return If(condition, body)

    def statement(self):
        """statement ::= assign | expr"""
        if self.cur_token.token_type == Token.NAME:
            if self.tokens.peek().token_type == Token.EQUAL:
                return self.assign()
            elif self.tokens.peek().token_type == Token.LPARAN:
                return self.condition_statement()
            return self.expr()

        else:
            return self.expr()

    def program(self):
        """program ::= statement { '\\n' statement }"""
        nodes = [self.statement()]
        while self.cur_token.token_type == Token.NEWLINE:
            self.eat(Token.NEWLINE)
            if self.cur_token.token_type == Token.EOF:
                break
            nodes.append(self.statement())
        return nodes

    def parse(self):
        nodes = self.program()
        return Module(self.name, nodes, self.constants, self.vars)
