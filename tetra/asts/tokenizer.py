"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from lib2to3.pgen2.token import NEWLINE
from .tokens import *
import re, typing

# Windows uses \r\n, Linux uses \n and Mac uses \r
regexs ={"NUMBER": r'\d+', "PLUS": r'\+', "MINUS": r'-', "MUL": r'\*', "DIV": r'/', "LPARAN": r'\(', "RPARAN": r'\)', "NAME": r"(?!\d+)\w+", "EQUAL": r'=', "NEWLINE": r'(\r\n|\r|\n)', "STRING": r"""(["'])(?:(?=(\\?))\2.)*?\1"""}

IGNORE = r'(?=([^"\\]*(\\.|"([^"\\]*\\.)*[^"\\]*"))*[^"]*$)' # ignore everything in quotes, can be added to all regexs

regexs = {k: re.compile(v + IGNORE) for k, v in regexs.items()}

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
            self.index += 1 # We increment the index beforehand in "next" because after the return we wouldn't be able to increment the index.
            return self.tokens[self.index - 1]
    
    def peek(self):
        if self.index >= len(self.tokens):
            raise StopIteration
        else:
            return self.tokens[self.index]

    def peek_old(self):
        if self.index >= len(self.tokens) or self.index <= 1:
            raise StopIteration
        else:
            return self.tokens[self.index-2] # -1 is the current token, -2 is the previous token. 
    
    def __str__(self) -> str:
        return str(self.tokens)

class Tokenizer:
    """The tokenizer uses a regex to find all tokens in the source code. It sorts them by column, so that the parser can easily find the next token.
    """
    def __init__(self, source: str):
        self.source = source

    def parse_line(self, line, lineo) -> typing.List[TokenInfo]:
        tokens = []
        for i, regex in enumerate(regexs.values()):
            pos = 0
            while True:
                match = regex.search(line, pos)
                if match:
                    pos = match.end()
                    tokens.append(TokenInfo(getattr(Token, list(regexs.keys())[i]), match.group(0), line, lineo, match.start()))
                else:
                    break
        tokens.sort(key=lambda x: x.column)
        tokens.append(TokenInfo(Token.NEWLINE, None, line, lineo, len(line)))
        return tokens
    def parse_source(self) -> typing.List[TokenInfo]:
        tokens = []
        for i, line in enumerate(self.source.splitlines()):
            tokens.extend(self.parse_line(line, i+1)) # +1 because line numbers start at 1
        return tokens
    def tokenize(self) -> TokenStream: 
        tokens = self.parse_source()
        tokens.append(TokenInfo(Token.EOF, None, "", tokens[-1].lineo + 1 if tokens else "", 0))
        return TokenStream(tokens)
