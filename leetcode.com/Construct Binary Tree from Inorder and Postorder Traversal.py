"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Construct Binary Tree from Inorder and Postorder Traversal
"""
from typing import List
from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inStart, inEnd, postStart, postEnd):
            if inStart > inEnd:
                return None

            root = TreeNode(postorder[postEnd])
            inorderIndex = inorder.index(root.val)
            leftSize = inorderIndex - inStart

            root.left = build(inStart, inorderIndex - 1, postStart, postStart + leftSize - 1)
            root.right = build(inorderIndex + 1, inEnd, postStart + leftSize, postEnd - 1)

            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)


class Case(TestCase):
    s = Solution()

    def test_case_1(self):
        actual = self.s.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
        expected = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(actual, expected)
