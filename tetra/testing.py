"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from asts.ast import Parser
from asts.tokens import Token, TokenInfo
from asts.tokenizer import TokenStream
from bytecode.parser import Parser as BytecodeParser
from bytecode.opcodes import Opcode
import tetra
from asts.tokenizer import *

tokens = Tokenizer("1 + 2 * 3").tokenize()

parser = Parser(tokens)

code = BytecodeParser(parser.parse()).parse()
code.bytecode.append((Opcode.DUMP, None))

tetra.Interpreter(code).run()