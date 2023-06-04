"""
https://leetcode.com/problems/minimum-cost-for-tickets/
Minimum Cost For Tickets
"""
from functools import lru_cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(maxsize=None)
        def calc(last_day: int):
            nonlocal days, costs
            if last_day < days[0]:
                return 0
            if last_day not in days:
                for day in reversed(days):
                    if last_day >= day:
                        last_day = day
                        break
            return min(
                calc(last_day - 1) + costs[0],
                calc(last_day - 7) + costs[1],
                calc(last_day - 30) + costs[2]
            )

        return calc(days[-1])


s = Solution()
assert s.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]) == 11
