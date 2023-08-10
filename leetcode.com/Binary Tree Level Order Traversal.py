"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
Binary Tree Level Order Traversal
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def write(node, level):
            nonlocal res
            if node is None: return
            if len(res) < level + 1:
                res.append([])

            res[level].append(node.val)

            write(node.left, level + 1)
            write(node.right, level + 1)

        write(root, 0)

        return res
