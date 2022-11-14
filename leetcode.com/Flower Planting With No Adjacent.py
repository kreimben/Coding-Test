"""
Flower Planting With No Adjacent
https://leetcode.com/problems/flower-planting-with-no-adjacent/
"""
from collections import defaultdict
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        res = [0] * n

        for a, b in paths:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(1, n + 1):
            neighbours = graph[i]
            for j in range(1, 5):
                # 1, 2, 3, 4
                for val in neighbours:
                    if j == res[val - 1]: break
                else:
                    # if not exists,
                    res[i - 1] = j
                    break

        return res


s = Solution()
assert s.gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]]) == [1, 2, 3]
