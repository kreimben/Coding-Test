"""
Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/
"""
from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # make a graph cuz problem don't give a graph class.
        graph = defaultdict(list)
        for tar, dep in edges:
            graph[tar].append(dep)

        # first, check if every graph is connected. (in BFS)
        count = 0
        q = []
        visited = set()

        def bfs() -> bool:
            nonlocal count, q, graph, visited
            while q:
                val = q.pop(0)
                for n in graph[val] if val in graph else []:
                    if n in visited: return False
                    visited.add(n)
                    q.append(n)
            count += 1
            return True

        for i in edges:
            if i[0] in visited: continue
            visited.add(i[0])
            q.append(i[0])
            res = bfs()
            if not res: return False

        if count != 1:
            return False
        else:
            return True


s = Solution()
assert s.validTree(4, [[0, 1], [2, 3]]) == False
assert s.validTree(2, [[1, 0]]) == True
