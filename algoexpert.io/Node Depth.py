"""
https://www.algoexpert.io/questions/node-depths
Node Depth
"""
from functools import reduce


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_depth(root: BinaryTree, level: int, sum: [int]):
    if root is not None:
        if root.left is not None:
            count_depth(root.left, level + 1, sum)

        if root.right is not None:
            count_depth(root.right, level + 1, sum)

        sum.append(level)


def nodeDepths(root: BinaryTree):
    level = 0
    sum = []

    count_depth(root, level, sum)

    return reduce(lambda x, y: x + y, sum)


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right = BinaryTree(5)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

assert nodeDepths(root) == 16
