"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Count Good Nodes in Binary Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # integer root.value to maximum value.
        # I should find them.
        result = 1

        def count(node, maxval):
            nonlocal result
            if node is None:
                return
            if node.val >= maxval:
                maxval = node.val
                result += 1
            count(node.left, maxval)
            count(node.right, maxval)

        count(root.left, root.val)
        count(root.right, root.val)
        return result
