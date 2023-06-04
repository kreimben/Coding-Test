"""
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
Longest ZigZag Path in a Binary Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = []

        def count(node, past, n):
            nonlocal res
            if node is None:
                res.append(n - 1)
                return

            if past == 'left':
                count(node.left, 'left', 1)
            else:
                count(node.left, 'left', n + 1)

            if past == 'right':
                count(node.right, 'right', 1)
            else:
                count(node.right, 'right', n + 1)

        count(root.left, 'left', 1)
        count(root.right, 'right', 1)

        return max(res)
