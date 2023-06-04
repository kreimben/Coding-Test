"""
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
Minimum Score of a Path Between Two Cities
"""
from cmath import inf
from collections import defaultdict, deque
from typing import List


# class Solution:
#     """
#     이렇게 풀면 시간 초과가 나는데
#     이렇게 푼 이유는 1부터 n까지 연결 됐다는 증거를 찾지 못했기 때문이다.
#     """
#     def minScore(self, n: int, roads: List[List[int]]) -> int:
#         roads.sort(key=lambda x: x[2])
#
#         maxheight = 0
#         for s, e, _ in roads:
#             maxheight = max(maxheight, s, e)
#         graph = [[0 for _ in range(maxheight + 1)] for _ in range(maxheight + 1)]
#
#         for s, e, d in roads:
#             graph[s][e] = d
#             graph[e][s] = d
#
#         @lru_cache(maxsize=None)
#         def is_connected(target: int, find: int) -> bool:
#             nonlocal graph
#             # The only thing this function has to do is traverse a graph to find target.
#             targets = [target]
#             visited = set()
#             while targets:
#                 next_target = targets.pop()
#                 if graph[next_target][find]:
#                     return True
#                 else:
#                     for i, n in enumerate(graph[next_target]):
#                         if n != 0 and i not in visited:
#                             targets.append(i)
#                             visited.add(i)
#             return False
#
#         for one, two, distance in roads:  # Because `roads` is already sorted. I can traverse this array.
#             # if one is connected with n or two do, Return distance.
#             if is_connected(target=n, find=one) or is_connected(target=n, find=two):
#                 return distance
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w

        res = inf
        vis = set()
        dq = deque([1])

        while dq:
            node = dq.popleft()
            for adj, scr in graph[node].items():
                if adj not in vis:
                    dq.append(adj)
                    vis.add(adj)
                res = min(res, scr)

        return res
