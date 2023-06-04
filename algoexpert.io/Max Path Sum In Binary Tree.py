"""
https://www.algoexpert.io/questions/max-path-sum-in-binary-tree
Max Path Sum In Binary Tree
"""


def maxPathSum(head):
    sums = []

    def count(tree, sums):
        if not tree:
            return 0  # Because there are no nodes.

        left = count(tree.left, sums)
        right = count(tree.right, sums)

        sums.append(max(tree.value + left, tree.value + right, tree.value + left + right))

        return max(tree.value + left, tree.value + right)

    left = count(head.left, sums)
    right = count(head.right, sums)
    return max(head.value + left + right, head.value + left, head.value + right, *sums)


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
        self.assertEqual(18, maxPathSum(test))

    def test_case_2(self):
        test = BinaryTree(1).insert([2, -1])
        self.assertEqual(maxPathSum(test), 3)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.value} ({self.left} / {self.right})'

    def __repr__(self):
        return f'{self.value} ({self.left} / {self.right})'

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self
