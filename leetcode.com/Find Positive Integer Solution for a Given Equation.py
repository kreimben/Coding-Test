"""
https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/description/
Find Positive Integer Solution for a Given Equation
"""
from typing import List


class CustomFunction:
    """
       This is the custom function interface.
       You should not implement it, or speculate about its implementation
    """

    def f(self, x, y):
        # Returns f(x, y) for any given positive integers x and y.
        # Note that f(x, y) is increasing with respect to both x and y.
        # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
        pass


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = set()

        for i in range(1, 501):
            for j in range(1, 501):
                if customfunction.f(i, j) == z:
                    res.add((i, j))
                    if customfunction.f(j, i) == z:
                        res.add((j, i))

        return list(res)
