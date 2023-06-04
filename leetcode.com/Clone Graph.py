"""
https://leetcode.com/problems/clone-graph/
Clone Graph
"""
"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        def count(array, target):
            c = 0
            for num in array:
                if num == target:
                    c += 1
            return c

        if node is None:
            return None

        root = Node()  # root is just dummy

        visited = []  # can save values cuz each node's value is unique.

        def backup(node, curr):
            nonlocal visited
            visited.append(node.val)
            curr.neighbors.append(Node(node.val))

            for n in node.neighbors:
                if count(visited, n.val) >= 2:
                    backup(n, curr.neighbors[0])

        backup(node, root)
        return root.neighbors[0]
