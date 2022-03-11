"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""
from dis import Bytecode
from tetra.ast.ast import Parser
from tetra.ast.tokens import Token, TokenInfo
from tetra.ast.tokenizer import TokenStream
from tetra.bytecode.parser import Parser as BytecodeParser
from tetra.bytecode.opcodes import Opcode
import tetra.tetra as tetra
from tetra.ast.tokenizer import *

tokens = Tokenizer("1 + 2 * 3").tokenize()

parser = Parser(tokens)

code = BytecodeParser(parser.parse()).parse()
code.bytecode.append((Opcode.DUMP, None))

tetra.Interpreter(code).run()