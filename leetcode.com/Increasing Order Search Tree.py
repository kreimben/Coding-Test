"""
Increasing Order Search Tree
https://leetcode.com/problems/increasing-order-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(0)
        curr = dummy

        def traverse(node: TreeNode):
            nonlocal curr

            if node is None: return

            traverse(node.left)

            curr.right = TreeNode(node.val)
            curr = curr.right

            traverse(node.right)

        traverse(root)

        return dummy.right
