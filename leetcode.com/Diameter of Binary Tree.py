"""
https://leetcode.com/problems/diameter-of-binary-tree/description/
Diameter of Binary Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxval = 0

        def count(node):
            nonlocal maxval

            if node is None:
                return 0
            # Divide and Conquor
            # Get depth of left and right child.
            # And return largest value of sum of it's child nodes.
            left = count(node.left)
            right = count(node.right)

            maxval = max(maxval, left + right)

            if left + right == 0:
                return 1
            else:
                return max(left, right) + 1

        count(root)

        return maxval
