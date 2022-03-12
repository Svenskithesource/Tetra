"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from .bytecode.opcodes import *
from .bytecode.parser import Code
from .asts.ast import Parser
from .asts.tokens import Token, TokenInfo
from .asts.tokenizer import *
from .bytecode.parser import Parser as BytecodeParser
import typing

class Interpreter:
    """The interpreter is a stack based machine. It is inspired by Python's interpreter, as in saving the constants in a separate list and then pushing them on the stack.
    It expects a code object as all information needed to run the program is saved here."""
    def __init__(self, source: str):
        self.source = source
        self.stack = [] 

    def run(self):
        tokens = Tokenizer(self.source).tokenize()

        parser = Parser(tokens)

        code = BytecodeParser(parser.parse()).parse()

        self.code = code
        return self.execute()

    def execute(self):
        for opcode in self.code.bytecode:
            if opcode[0] == Opcode.ADD:
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a + b)
            elif opcode[0] == Opcode.SUB:
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(b - a) # b - a because the top item on the stack is the right operand
            elif opcode[0] == Opcode.MUL:
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a * b)
            elif opcode[0] == Opcode.DIV:
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(b // a) # we use // (floor division) because we only support integers for now, also raises an ZeroDivisionError if b == 0 (done by Python)
            elif opcode[0] == Opcode.LOAD_CONST:
                self.stack.append(self.code.consts[opcode[1]])
            elif opcode[0] == Opcode.DUMP:
                print(self.stack.pop())
        
        return self.stack.pop() # the last item on the stack is the result of the program
            
