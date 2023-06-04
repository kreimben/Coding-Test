"""
https://leetcode.com/problems/binary-tree-right-side-view/
Binary Tree Right Side View
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> [int]:
        result = []

        def count(node, level):
            if node is None:
                return
            if len(result) <= level:
                result.append([(level, node.val)])
            else:
                result[level].append((level, node.val))
            count(node.left, level + 1)
            count(node.right, level + 1)

        count(root, 0)

        return [v[-1][1] for v in result]
