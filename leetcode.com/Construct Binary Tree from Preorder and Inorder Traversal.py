"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
Construct Binary Tree from Preorder and Inorder Traversal
"""
from idlelib.tree import TreeNode
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
