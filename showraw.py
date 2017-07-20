""" Show rawsource
"""
from __future__ import print_function

from docutils.nodes import SparseNodeVisitor


class ShowRaw(SparseNodeVisitor):

    def visit_Text(self, node):
        print('rawsource is', node.rawsource, ';')
        print('astext() is', node.astext(), ';')

    def unknown_visit(self, node):
        pass


def dt_show_raw(app, doctree):
    doctree.walk(ShowRaw(doctree.document))


def setup(app):
    app.connect("doctree-read", dt_show_raw)
