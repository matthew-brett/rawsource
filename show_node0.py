from __future__ import print_function

from os.path import join as pjoin
import pickle
with open(pjoin('_build', 'doctrees', 'index.doctree'), 'rb') as fobj:
    tree = pickle.load(fobj)
node = tree.children[0]
print('node.rawsource', node.rawsource)
