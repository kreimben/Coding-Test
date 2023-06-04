"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
Lowest Common Ancestor of a Binary Search Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def find_and_make_chain(node, target):
            chain = []
            curr = node
            while curr:
                chain.append(curr)
                if curr.val == target.val:
                    break
                elif curr.val >= target.val:
                    curr = curr.left
                else:
                    curr = curr.right
            return chain

        first = find_and_make_chain(root, p)  # 6, 2 # 6, 2
        # print(f'{[node.val for node in first]}')
        second = find_and_make_chain(root, q)  # 6, 8 # 6, 2, 4
        # print(f'{[node.val for node in second]}')
        # I have to get the last same value while traversing array (chain).
        prev = None
        for i in range(min(len(first), len(second))):
            if prev is None:  # probably i should be 0.
                prev = first[i]
            elif first[i].val == second[i].val:
                prev = first[i]
            else:
                break
        return prev
