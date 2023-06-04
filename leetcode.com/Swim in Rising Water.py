"""
https://leetcode.com/problems/swim-in-rising-water/
Swim in Rising Water
"""
import heapq
from typing import List
from unittest import TestCase


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        s = [(grid[0][0], 0, 0)]
        visited = set()
        direction = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        visited.add((0, 0))
        while s:
            val, x, y = heapq.heappop(s)
            visited.add((x, y))

            if x == n - 1 and y == n - 1:
                return val

            for ai, aj in direction:
                i = ai + x
                j = aj + y

                if i < 0 or j < 0 or i == n or j == n or (i, j) in visited:
                    continue
                heapq.heappush(
                    s,
                    (max(val, grid[i][j]), i, j)
                )
                visited.add((i, j))


class Test(TestCase):
    s = Solution()

    def test_case_1(self):
        actual = self.s.swimInWater(
            [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
        )
        expected = 16
        self.assertEqual(actual, expected)


t = Test()
t.test_case_1()
