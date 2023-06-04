"""
https://leetcode.com/problems/k-closest-points-to-origin/
K Closest Points to Origin
"""
import heapq
from math import sqrt
from typing import List


class Solution:
    def distance(self, x: int, y: int) -> float:
        return sqrt(x ** 2 + y ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        s = []
        for x, y in points:
            heapq.heappush(s, (-self.distance(x, y), (x, y)))
            if len(s) > k:
                heapq.heappop(s)
        return [(x, y) for _, (x, y) in s]


s = Solution()
assert s.kClosest([[1, 3], [-2, 2]], 1) == [1, 3]
