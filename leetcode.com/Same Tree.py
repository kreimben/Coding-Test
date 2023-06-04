"""
https://leetcode.com/problems/same-tree/description/
Same Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def count(n1, n2):
            if n1 is None and n2 is None:
                return True
            elif ((n1 and not n2) or (n2 and not n1)) or n1.val != n2.val:
                return False

            lr = count(n1.left, n2.left)
            rr = count(n1.right, n2.right)

            if lr is False or rr is False:
                return False
            else:
                return True

        return count(p, q)
