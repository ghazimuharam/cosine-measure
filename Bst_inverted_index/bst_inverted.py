import os
from Bst import BinarySearchTree

biTree = BinarySearchTree()
r = biTree.root

DOC_DIR = '../Documents'
docs = sorted(os.listdir(DOC_DIR))

docs_index = {}
inv_index = {}

for idx, doc in enumerate(docs):
    f = open(DOC_DIR+'/'+doc, 'r')
    docs_index[idx] = doc
    tokens = f.read().lower().strip().split(' ')
    pad = 0
    for token in tokens:
        if token in biTree.stopwords:
            continue
        biTree.insert(token, pad, idx)
        pad = pad + len(token)+1

biTree.inorder()
print(docs_index)
