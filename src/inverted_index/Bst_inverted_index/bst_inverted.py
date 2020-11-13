import os
from Bst import BinarySearchTree

biTree = BinarySearchTree()
r = biTree.root

DOC_DIR = '../Documents2'
docs = sorted(os.listdir(DOC_DIR))

docs_index = {}
inv_index = {}

for idx, doc in enumerate(docs):
    f = open(DOC_DIR+'/'+doc, 'r')
    docs_index[idx] = doc
    tokens = f.read().lower().strip().split(' ')
    pad = 0
    tokens = [x for x in tokens if x not in biTree.stopwords]
    for token in tokens:
        biTree.insert(token, pad, idx+1)
        pad = pad + len(token)+1

biTree.inorder()
print(docs_index)
