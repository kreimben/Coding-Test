"""
https://leetcode.com/problems/validate-binary-search-tree/
Validate Binary Search Tree
"""
from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, minimum, maximum) -> bool:
            if node is None:
                return True
            elif node.val <= minimum or maximum <= node.val:
                return False
            else:
                return check(node.left, minimum, node.val) and \
                    check(node.right, node.val, maximum)

        return check(root, -inf, inf)
