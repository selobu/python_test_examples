class Node:
    def __init__(self, value):
        self.value = value
        self._left = None
        self._right = None

    def set_left(self, left):
        self._left = left
        return self

    def set_right(self, right):
        self._right = right
        return self

    @property
    def left(self):
        return self._left

    @property
    def rigth(self):
        return self._right

    @property
    def hasleft(self):
        if self._left is not None:
            return True
        return False

    @property
    def hasright(self):
        if self._right is not None:
            return True
        return False

    def __str__(self):
        return f"{self.value}"


def printTree(tree):
    if tree.hasleft:
        printTree(tree.left)
    if tree.hasright:
        printTree(tree.rigth)
    print(tree.value)


tree = (
    Node(10)
    .set_left(Node(5).set_left(Node(2)).set_right(Node(7).set_left(Node(5))))
    .set_right(Node(23).set_left(Node(18)).set_right(Node(31)))
)

printTree(tree)
