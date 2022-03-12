"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from .tokens import *
import re, typing

NUMBER = re.compile(r'\d')
PLUS = re.compile(r'\+')
MINUS = re.compile(r'-')
MUL = re.compile(r'\*')
DIV = re.compile(r'/')

ALL = {"NUMBER": NUMBER, "PLUS": PLUS, "MINUS": MINUS, "MUL": MUL, "DIV": DIV}

class TokenStream:
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

        return tokens
            
    def tokenize(self) -> TokenStream: 
        tokens = self.parse_line(self.source, 0)
        tokens.append(TokenInfo(Token.EOF, None, 0, 0))
        return TokenStream(tokens)



# parse("2 + 2")
# -> [TokenInfo(Token.NUMBER, 2, 1, 0), TokenInfo(Token.PLUS, '+', 1, 3), TokenInfo(Token.NUMBER, 2, 1, 5)]