"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/
Sum Root to Leaf Numbers
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        values = []

        def count(node, chain):
            if node is None:
                return
            elif node.left is None and node.right is None:
                # It is final.
                c = chain + [str(node.val)]
                nonlocal values
                values.append(
                    int(''.join(c))
                )
            else:
                # If node has left child or right child.
                count(node.left, chain + [str(node.val)])
                count(node.right, chain + [str(node.val)])

        count(root, [])
        return sum(values)
