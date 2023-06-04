"""
https://leetcode.com/problems/balanced-binary-tree/description/
Balanced Binary Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def count(node):
            if node is None:
                return 0, True

            left, lb = count(node.left)
            right, rb = count(node.right)

            if lb and rb and abs(left - right) <= 1:
                return max(left, right) + 1, True
            else:
                return -1, False  # Because it is not balanced.

        _, balanced = count(root)

        return balanced
