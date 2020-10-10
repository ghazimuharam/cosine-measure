class Node(object):
    """
    docstring
    """

    def __init__(self, term, pd):
        self.left = None
        self.right = None
        self.term = term
        self.pd = [pd]

    def insertNode(self, term, pad, doc_id):
        if self.term == term:
            self.insertPD([pad, doc_id])
        elif self.term < term:
            if self.isEmptyRight():
                self.right = Node(term, [pad, doc_id])
                return
            self.right.insertNode(term, pad, doc_id)
        elif self.term > term:
            if self.isEmptyLeft():
                self.left = Node(term, [pad, doc_id])
                return
            self.left.insertNode(term, pad, doc_id)

    def isEmptyLeft(self):
        if (self.left is None):
            return True
        else:
            return False

    def isEmptyRight(self):
        if (self.right is None):
            return True
        else:
            return False

    def insertPD(self, pd):
        self.pd.insert(0, pd)

    def nodePrint(self):
        if not (self.isEmptyLeft()):
            self.left.nodePrint()
        print({'term': self.term, 'pd': self.pd})
        if not (self.isEmptyRight()):
            self.right.nodePrint()
