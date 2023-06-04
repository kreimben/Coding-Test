"""
https://www.algoexpert.io/questions/evaluate-expression-tree
Evaluate Expression Tree
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


import math


def evaluateExpressionTree(tree):
    operations = [-1, -2, -3, -4]

    def count(node):
        nonlocal operations
        if node is None:
            return
        if node.value in operations:
            if node.left.value in operations:
                node.left.value = count(node.left)
            if node.right.value in operations:
                node.right.value = count(node.right)
            # yes it's operation!
            if node.value == -1:
                return node.left.value + node.right.value
            elif node.value == -2:
                return node.left.value - node.right.value
            elif node.value == -3:
                s = node.left.value / node.right.value
                if s > 0:
                    return math.floor(s)
                else:
                    return math.ceil(s)
            elif node.value == -4:
                return node.left.value * node.right.value
        else:
            return node.value

    return count(tree)
