"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
Kth Smallest Element in a BST
"""
import heapq
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def count(node):
            nonlocal res, k
            if len(res) >= k:
                return
            if node is None:
                return
            count(node.left)
            res.append(node.val)
            count(node.right)

        count(root)
        return res[k - 1]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = []

        def traverse(node):
            nonlocal q
            if node is None:
                return
            q.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        heapq.heapify(q)

        res = 0
        while k:
            res = heapq.heappop(q)
            k -= 1

        return res
