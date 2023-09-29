"""
Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
"""
from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)

        # count with BFS.
        count = 0
        visited = set()
        q = []

        def bfs(start):
            nonlocal count, visited, q
            while q:
                ele = q.pop(0)
                for num in graph[ele]:
                    if num not in visited:
                        q.append(num)
                        visited.add(num)
            count += 1

        for i in range(n):
            if i in visited: continue
            visited.add(i)
            q.append(i)
            bfs(i)

        return count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # solve with union-find
        check = [i for i in range(n)]

        def find(child) -> int:
            nonlocal check
            if check[child] != child:
                return find(check[child])
            return child

        def union(parent, child):
            nonlocal check
            p = find(parent)
            c = find(child)
            check[c] = p

        for parent, child in edges:
            union(parent, child)

        res = defaultdict(int)
        for i in range(n):
            res[find(i)] += 1

        return len(res.keys())


s = Solution()
assert s.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
