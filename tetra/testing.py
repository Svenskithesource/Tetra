"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from tetra.tetra import Interpreter, Code
from tetra.opcodes import Opcode

interpreter = Interpreter(Code(bytecode=[(Opcode.LOAD_CONST, 0), (Opcode.LOAD_CONST, 1), (Opcode.SUB,), (Opcode.DUMP,)], consts=[1, 2, 3]))
interpreter.run()