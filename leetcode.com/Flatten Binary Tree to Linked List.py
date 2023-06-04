"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
Flatten Binary Tree to Linked List
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        TO_BE_ALIGNED = 'to be aligned'
        """
        Do not return anything, modify root in-place instead.
        """

        def align(node, oposite):
            if node is None:
                return None, True

            node.left, is_left_none = align(node.left, 'left')  # wrap up left first!
            if node.left and node.right:
                if is_left_none == TO_BE_ALIGNED:
                    curr = node.left
                    while curr.right:
                        curr = curr.right
                    curr.right = node.right
                    node.right = node.left
                    node.left = None
            elif node.left and not node.right:
                node.right = node.left
                node.left = None

            node.right, is_right_none = align(node.right, 'right')

            if is_left_none is True and is_right_none is True and oposite == 'left':
                # there are nothing to be aligned.
                # tell parent node to move to right node if i'm in left node.
                return node, TO_BE_ALIGNED

            return node, TO_BE_ALIGNED

        root, _ = align(root, '')
