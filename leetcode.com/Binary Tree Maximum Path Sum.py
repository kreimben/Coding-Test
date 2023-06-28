"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
Binary Tree Maximum Path Sum
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        arr = []

        def count(node: TreeNode) -> int:
            nonlocal arr

            if node is None:
                return 0

            left = count(node.left) + (node.left.val if node.left else 0)
            right = count(node.right) + (node.right.val if node.right else 0)

            arr.append(max(left + right + node.val, left + node.val, right + node.val, node.val))
            return max(left, right, 0)

        count(root)

        return max(arr)
