"""
Detect Squares
https://leetcode.com/problems/detect-squares/description/
"""
from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.pointcount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointcount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.pointcount[(x, py)] * self.pointcount[(px, y)]
        return res
