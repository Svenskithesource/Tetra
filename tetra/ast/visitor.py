class NodeVisitor:
    """A node visitor that walks the AST. The bytecode parser will use this to walk through and generate the bytecode.
    """
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name)
        return visitor(node)

