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
        result = []

        def count(node, level):
            nonlocal result
            if node is None:
                return

            if len(result) > level:
                if result[level]:
                    result[level].append(node.val)
                else:
                    result[level] = [node.val]
            else:
                result.append([node.val])

            count(node.left, level + 1)
            count(node.right, level + 1)

        count(root, 0)

        return result
