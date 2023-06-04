"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
Reorder Routes to Make All Paths Lead to the City Zero
"""
from collections import defaultdict
from typing import List


# class Solution:
#     """
#     이렇게 써도 정답이긴 한데
#     TLE뜨니깐 전체 테이블로 순환하는것 보다
#     dictionary안에 list를 넣어 traverse하도록 하자.
#     """
#
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         connections.sort()
#         count = 0
#
#         table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#         for dep, arr in connections:
#             table[arr][dep] = table[dep][arr] = 1  # mark up as undirected graph
#
#         def dfs(target: int, visited: List[int]):
#             nonlocal table, count, n
#             for i, val in enumerate(table[target]):
#                 if val == 1 and i not in visited:
#                     if [target, i] in connections:  # If direction is reversed.
#                         count += 1
#                     dfs(i, visited + [i])
#
#         dfs(0, [0])
#
#         return count


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0
        roads = set()
        graph = defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)

        def dfs(u, parent):
            self.res += (parent, u) in roads
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)

        dfs(0, -1)
        return self.res


s = Solution()
assert s.minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
