# Copyright (c) 2013 Huan Do, http://huan.do

import ast

from also import also, AlsoMetaClass

class FutureFinder(ast.NodeVisitor):
    __metaclass__ = AlsoMetaClass

    def __init__(self, env):
        self.future_import_nodes = []

    def visit_ImportFrom(self, node):
        if node.module == '__future__':
            self.future_import_nodes.append(node)
