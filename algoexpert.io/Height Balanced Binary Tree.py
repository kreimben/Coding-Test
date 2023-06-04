"""
https://www.algoexpert.io/questions/height-balanced-binary-tree
Height Balanced Binary Tree
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'


def heightBalancedBinaryTree(tree):
    def check(tree):
        if tree is None:
            return -1, True  # Because it's balanced.

        lheight, lcheck = check(tree.left)
        rheight, rcheck = check(tree.right)

        is_balanced = lcheck and rcheck and abs(lheight - rheight) <= 1
        height = max(lheight, rheight) + 1

        return height, is_balanced

    _, ccheck = check(tree)

    return ccheck


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.left.right.left = BinaryTree(7)
root.left.right.right = BinaryTree(8)
root.right.right = BinaryTree(6)
root.right.right.left = BinaryTree(9)
root.right.right.right = BinaryTree(10)

expected = True
actual = heightBalancedBinaryTree(root)
assert actual == expected
