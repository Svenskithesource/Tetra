"""
An interpreted language

Created by: svenskithesource (https://github.com/Svenskithesource), Jaxp (https://github.com/jaxp2)
"""

from .opcodes import *
from ..asts.ast import *
from ..asts.visitor import NodeVisitor
import typing

class Code:
    """All information about the code.
    The bytecode is a list of tuples, where the first item is the opcode and the second item is the index to the constant in the consts list.
    This object will be generated by the bytecode parser."""
    def __init__(self, name: str, bytecode: typing.List[typing.Union[Opcode, typing.Optional[int]]], consts: typing.List[int], vars: typing.List[str]): # Second item in the tuple is the index to the constant in the consts list
        self.name = name
        self.bytecode = bytecode
        self.consts = consts
        self.vars = vars
    
    def __str__(self):
        return f"Code(name={self.name}, bytecode={self.bytecode}, consts={self.consts})"

class Parser(NodeVisitor):
    """The parser is a visitor that generates the code object."""
    def __init__(self, ast: Module):
        self.ast = ast
        self.bytecode = []
    
    def visit_Module(self, node: Module):
        for child in node.body:
            self.visit(child)
    
    def visit_String(self, node: String):
        self.bytecode.append((Opcode.STORE_STRING, node.index))
    
    def visit_IntegerLiteral(self, node: IntegerLiteral):
        self.bytecode.append((Opcode.LOAD_CONST, node.index))
    
    def visit_Add(self, node: Add):
        self.visit(node.left)
        self.visit(node.right)
        self.bytecode.append((Opcode.ADD, None))
    
    def visit_Sub(self, node: Sub):
        self.visit(node.left)
        self.visit(node.right)
        self.bytecode.append((Opcode.SUB, None))
    
    def visit_Mul(self, node: Mul):
        self.visit(node.left)
        self.visit(node.right)
        self.bytecode.append((Opcode.MUL, None))
    
    def visit_Div(self, node: Div):
        self.visit(node.left)
        self.visit(node.right)
        self.bytecode.append((Opcode.DIV, None))

    def visit_Store(self, node: Store):
        self.visit(node.value)
        self.bytecode.append((Opcode.STORE_VAR, node.index))

    def visit_Load(self, node: Load):
        self.bytecode.append((Opcode.LOAD_VAR, node.index))

    def parse(self) -> Code:
        self.visit(self.ast)
        return Code(self.ast.name, self.bytecode, self.ast.constants, self.ast.vars)

