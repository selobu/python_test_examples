class Node:
    def __init__(self, value):
        self.value = value
        self._left = None
        self._right = None
    @property
    def hasLeft(self):
        return self._left is not None
    @property
    def hasRigth(self):
        return self._right is not None
    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right
    def set_left(self, left):
        self._left = left
        return self
    def set_right(self, right):
        self._right = right
        return self

def printTree(tree):
    if tree.hasLeft:
        printTree(tree.left)
    if tree.hasRigth:
        printTree(tree.right)
    print(tree.value)

tree = Node(10)\
    .set_left(
        Node(5)\
            .set_left(Node(2))\
            .set_right(
                Node(7)\
                .set_left(Node(5))
                )
        )\
    .set_right(
        Node(23)\
            .set_left(Node(18))\
            .set_right(Node(31))
        )

printTree(tree)