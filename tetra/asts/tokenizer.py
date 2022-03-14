"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from lib2to3.pgen2.token import NEWLINE
from .tokens import *
import re, typing

NUMBER = re.compile(r'\d+')
PLUS = re.compile(r'\+')
MINUS = re.compile(r'-')
MUL = re.compile(r'\*')
DIV = re.compile(r'/')
LPARAN = re.compile(r'\(')
RPARAN = re.compile(r'\)')
NAME = re.compile(r"(?!\d+)\w+")
EQUAL = re.compile(r'=')
NEWLINE = re.compile(r'(\r\n|\r|\n)') # Windows uses \r\n, Linux uses \n and Mac uses \r
ALL = {"NUMBER": NUMBER, "PLUS": PLUS, "MINUS": MINUS, "MUL": MUL, "DIV": DIV, "LPARAN": LPARAN, "RPARAN": RPARAN, "NAME": NAME, "EQUAL": EQUAL, "NEWLINE": NEWLINE}

class TokenStream:
    """Behaves like a generator
    """
    def __init__(self, tokens: typing.List):
        self.tokens = tokens
        self.index = 0
    
    def next(self):
        if self.index >= len(self.tokens):
            raise StopIteration
        else:
            self.index += 1
            return self.tokens[self.index - 1]
    
    def __str__(self) -> str:
        return str(self.tokens)

class Tokenizer:
    """The tokenizer uses a regex to find all tokens in the source code. It sorts them by column, so that the parser can easily find the next token.
    """
    def __init__(self,source: str):
        self.source = source
    def parse_line(self, line, lineo) -> typing.List[TokenInfo]:
        tokens = []
        for i, regex in enumerate(ALL.values()):
            pos = 0
            while True:
                match = regex.search(line, pos)
                if match:
                    pos = match.end()
                    tokens.append(TokenInfo(getattr(Token, list(ALL.keys())[i]), match.group(0), lineo, match.start()))
                else:
                    break
        tokens.sort(key=lambda x: x.column)
        tokens.append(TokenInfo(Token.NEWLINE, None, lineo, len(line)))
        return tokens
    def parse_source(self):
        tokens = []
        for i, line in enumerate(self.source.splitlines()):
            tokens.extend(self.parse_line(line, i+1)) # +1 because line numbers start at 1
        return tokens
    def tokenize(self) -> TokenStream: 
        tokens = self.parse_source()
        tokens.append(TokenInfo(Token.EOF, None, 0, 0))
        return TokenStream(tokens)
