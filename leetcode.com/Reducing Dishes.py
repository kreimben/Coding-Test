"""
https://leetcode.com/problems/reducing-dishes/description/
Reducing Dishes
"""
from functools import lru_cache
from typing import List


class Solution:
    """
    This is top-down approach to solve DP problem.
    """

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        if len(list(filter(lambda x: x >= 0, satisfaction))) == 0:
            return 0  # If people don't like the diches.

        satisfaction.sort()  # -9, -8, -1, 0, 5

        @lru_cache(maxsize=None)
        def count(index: int, time: int):
            nonlocal satisfaction
            if index >= len(satisfaction):
                return 0
            return max(
                count(index + 1, time + 1) + time * satisfaction[index],
                count(index + 1, time)
            )

        return count(index=0, time=1)


s = Solution()
assert s.maxSatisfaction([-1, -8, 0, 5, -9]) == 14
