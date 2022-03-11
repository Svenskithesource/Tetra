"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from tokens import *
import re, typing

def group(*regexs): return "(" + "|".join(regexs) + ")" # still dont get wat it does after this

NUMBER = r'\d'
PLUS = r'\+'
MINUS = r'-'
ALL = re.compile(group(NUMBER, PLUS, MINUS))

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

class Tokenizer:
    def __init__(self,source: str):
        self.source = source
    
    def parse_line(self, line, lineo) -> typing.List[re.Match]:
        tokens = []
        for match in ALL.finditer(line):
            print(match.re)
            # tokens.append(TokenInfo(Token.NUMBER, token.group(), token.start(), lineo))
        
        # (token.start(), token.group()) for token in re.finditer(r"\S+")
    def parse_file(self):
        for i, line in enumerate(self.source.splitlines()):
            self.parse_line(line, i)
            
    def tokenize(self) -> typing.List[TokenInfo]: 
        tokens = []

# parse("2 + 2")
# -> [TokenInfo(Token.NUMBER, 2, 1, 0), TokenInfo(Token.PLUS, '+', 1, 3), TokenInfo(Token.NUMBER, 2, 1, 5)]