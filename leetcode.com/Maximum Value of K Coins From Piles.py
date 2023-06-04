"""
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
Maximum Value of K Coins From Piles
"""
from functools import lru_cache
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        res = []

        @lru_cache
        def count(i, j, rest, skip_this, accu):
            nonlocal k, res
            if rest >= k or i >= len(piles) or j >= len(piles[i]):
                res.append(accu)
                return

            next_number = (i, j + 1) if j + 1 < len(piles[i]) and not skip_this else None
            skip_number = (i + 1, 0) if i + 1 < len(piles) else None

            if next_number:
                count(*next_number, rest + 1, False, accu + piles[next_number[0]][next_number[1]])
                count(*next_number, rest, True, accu)

            if skip_number:
                count(*skip_number, rest + 1, False, accu + piles[skip_number[0]][skip_number[1]])
                count(*skip_number, rest, True, accu)

        count(0, 0, 1, False, piles[0][0])
        count(0, 0, 0, True, 0)

        return max(res)


s = Solution()
assert s.maxValueOfCoins([[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7) == 706
assert s.maxValueOfCoins([[1, 100, 3], [7, 8, 9]], 2) == 101
