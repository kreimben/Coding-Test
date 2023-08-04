"""
Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/description/
"""
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(node) -> bool:
            if node is None:
                return False
            elif is_identical(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        def is_identical(o, s):
            if o is None or s is None:
                return o is None and s is None

            return o.val == s.val and is_identical(o.left, s.left) and is_identical(o.right, s.right)

        return dfs(root)
