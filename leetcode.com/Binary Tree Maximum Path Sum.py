"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
Binary Tree Maximum Path Sum
"""
import math
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional['TreeNode']) -> int:
        maxval = -math.inf

        def traverse(tree: 'TreeNode') -> int:
            nonlocal maxval
            if tree.left and tree.right:
                left = traverse(tree.left)
                right = traverse(tree.right)
                maxval = max(maxval, left + right + tree.val, left + tree.val, right + tree.val, left, right, tree.val)
                return max(max(left, right) + tree.val, tree.val)
            elif tree.left:
                left = traverse(tree.left)
                maxval = max(maxval, left + tree.val, left, tree.val)
                return max(tree.val, left + tree.val)
            elif tree.right:
                right = traverse(tree.right)
                maxval = max(maxval, right + tree.val, right, tree.val)
                return max(tree.val, right + tree.val)
            else:
                maxval = max(maxval, tree.val)
                return tree.val

        res = traverse(root)
        maxval = max(maxval, res)

        return maxval


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        arr = []

        def count(node: TreeNode) -> int:
            nonlocal arr

            if node is None:
                return 0

            left = count(node.left) + (node.left.val if node.left else 0)
            right = count(node.right) + (node.right.val if node.right else 0)

            arr.append(max(left + right + node.val, left + node.val, right + node.val, node.val))
            return max(left, right, 0)

        count(root)

        return max(arr)
