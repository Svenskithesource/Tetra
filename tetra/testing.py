"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""
from tetra.ast.ast import Parser
from tetra.ast.tokens import Token, TokenInfo
from tetra.ast.tokenizer import TokenStream

parser = Parser(TokenStream([TokenInfo(Token.NUMBER, 1, 0, 0), TokenInfo(Token.PLUS, "+", 0, 0), TokenInfo(Token.NUMBER, 2, 0, 0), TokenInfo(Token.MUL, "*", 0, 0), TokenInfo(Token.NUMBER, 2, 0, 0), TokenInfo(Token.EOF, None, 0, 0)]))