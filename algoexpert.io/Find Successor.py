"""
https://www.algoexpert.io/questions/find-successor
Find Successor
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f'{self.value}'


def findSuccessor(tree, node):
    if node.right is not None:
        curr = node.right
        while True:
            if curr.left is not None:
                curr = curr.left
            else:
                return curr

    child = node
    parent = node.parents
    while True:
        if parent is None or child is parent.left: return parent
        child = parent
        parent = parent.parents


root = BinaryTree(1)

root.left = BinaryTree(2)
root.left.parent = root
root.right = BinaryTree(3)
root.right.parent = root

root.left.left = BinaryTree(4)
root.left.left.parent = root.left
root.left.right = BinaryTree(5)
root.left.right.parent = root.left

root.left.right.left = BinaryTree(6)
root.left.right.left.parent = root.left.right
root.left.right.right = BinaryTree(7)
root.left.right.right.parent = root.left.right

root.left.right.right.left = BinaryTree(8)
root.left.right.right.left.parent = root.left.right.right

assert findSuccessor(root, root.left.right).value == 8
# assert findSuccessor(root, 11) == None
