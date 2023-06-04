"""
https://leetcode.com/problems/validate-binary-search-tree/
Validate Binary Search Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, root: TreeNode, p_max: int, p_min: int, results):
        if results[0] == False:
            return

        if not (p_min < root.val < p_max):
            results[0] = False
            return

        if root.left is not None:
            if root.left.val < root.val:
                self.check(root.left, root.val, p_min, results)
            else:
                results[0] = False

        if root.right is not None:
            if root.right.val > root.val:
                self.check(root.right, p_max, root.val, results)
            else:
                results[0] = False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        results = [True]
        self.check(root, float('inf'), float('-inf'), results)

        return results[0]
