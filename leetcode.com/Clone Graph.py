"""
https://leetcode.com/problems/clone-graph/
Clone Graph
"""
from collections import defaultdict

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self): return f'{self.val} {self.neighbors}'


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return node

        graph = defaultdict(set)

        def traverse(node):
            nonlocal graph
            for next in node.neighbors:
                if node.val not in graph[next.val] and next.val not in graph[node.val]:
                    graph[next.val].add(node.val)
                    graph[node.val].add(next.val)
                    traverse(next)

        traverse(node)

        nodes = [0] * len(graph)
        for num in graph:
            nodes[num - 1] = Node(num)

        for num in graph:
            for next in graph[num]:
                nodes[num - 1].neighbors.append(nodes[next - 1])

        return nodes[0] if nodes else Node(1)


# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if node is None: return node
#
#         elements: set[int] = set()
#         elements.add(node.val)
#
#         def count(node):
#             nonlocal elements
#             elements.add(node.val)
#             for next in node.neighbors:
#                 if next.val not in elements:
#                     count(next)
#
#         count(node)
#
#         nodes = [0] * len(elements)
#         for num in elements:
#             nodes[num - 1] = Node(num)
#
#         clone = Node(1)
#
#         def dfs(node, clone):
#             nonlocal nodes
#             for next in node.neighbors:
#                 if nodes[next.val - 1] not in clone.neighbors:
#                     clone.neighbors.append(
#                         nodes[next.val - 1]
#                     )
#                     dfs(next, clone.neighbors[-1])
#
#         dfs(node, clone)
#
#         return clone


s = Solution()
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.neighbors = [two, four]
two.neighbors = [one, three]
three.neighbors = [two, four]
four.neighbors = [one, three]
print(s.cloneGraph(one))

# class Solution:
#     def cloneGraph(self, node):
#         def count(array, target):
#             c = 0
#             for num in array:
#                 if num == target:
#                     c += 1
#             return c
#
#         if node is None:
#             return None
#
#         root = Node()  # root is just dummy
#
#         visited = []  # can save values cuz each node's value is unique.
#
#         def backup(node, curr):
#             nonlocal visited
#             visited.append(node.val)
#             curr.neighbors.append(Node(node.val))
#
#             for n in node.neighbors:
#                 if count(visited, n.val) >= 2:
#                     backup(n, curr.neighbors[0])
#
#         backup(node, root)
#         return root.neighbors[0]
