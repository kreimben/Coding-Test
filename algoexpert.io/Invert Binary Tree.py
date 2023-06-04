"""
https://www.algoexpert.io/questions/invert-binary-tree
Invert Binary Tree
"""


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
    def dfs(tree):
        tree.left, tree.right = tree.right, tree.left
        if tree.left is not None and (tree.left.left is not None or tree.left.right is not None):
            dfs(tree.left)
        if tree.right is not None and (tree.right.left is not None or tree.right.right is not None):
            dfs(tree.right)

    dfs(tree)


tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
invertedTree = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9])
invertBinaryTree(tree)
assert (tree.__eq__(invertedTree))
