from tetra import Interpreter, Code
from opcodes import Opcode

interpreter = Interpreter(Code(bytecode=[(Opcode.LOAD_CONST, 0), (Opcode.LOAD_CONST, 1), (Opcode.SUB,), (Opcode.DUMP,)], consts=[1, 2, 3]))
interpreter.run()