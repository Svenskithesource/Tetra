"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from opcodes import *
import typing

class Code:
    def __init__(self, bytecode: typing.List[typing.Union[Opcode, typing.Optional[int]]], consts: typing.List[int]): # Second item in the tuple is the index to the constant in the consts list
        self.bytecode = bytecode
        self.consts = consts

class Interpreter:
    def __init__(self, code: Code):
        self.code = code
        self.stack = [] 

    def run(self):
        for opcode in self.code.bytecode:
            if opcode[0] == Opcode.ADD:
                a = self.stack.pop() 
                b = self.stack.pop() 
                self.stack.append(a + b)
            elif opcode[0] == Opcode.SUB:
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(a - b) # TODO: Check if it doesn't have to be `b - a`
            elif opcode[0] == Opcode.LOAD_CONST:
                self.stack.append(self.code.consts[opcode[1]])
            elif opcode[0] == Opcode.DUMP:
                print(self.stack.pop())
            


