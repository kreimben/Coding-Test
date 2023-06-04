"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/
Min Cost Climbing Stairs
"""
from typing import List


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         dp = [0 for _ in range(len(cost) + 1)]
#
#         for i in range(1, len(cost) + 1):
#             if i == 1:
#                 dp[i] = cost[i - 1]
#             else:
#                 dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i - 1]
#
#         return min(dp[len(dp) - 1], dp[len(dp) - 2])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost.copy()

        for i, val in enumerate(cost[2:]):
            index = i + 2
            dp[index] = min(dp[index - 1] + val, dp[index - 2] + val)

        return min(dp[-1], dp[-2])


s = Solution()
assert s.minCostClimbingStairs([10, 15, 20]) == 15
assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
