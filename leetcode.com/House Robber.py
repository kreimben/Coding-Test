"""
https://leetcode.com/problems/house-robber/
House Robber
"""
from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i) -> int:
            if i > len(nums) - 1: return 0
            return max(
                dp(i + 2),
                dp(i + 3)
            ) + nums[i]

        return max(dp(0), dp(1))


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         dp = [0 for _ in range(len(nums) + 1)]
#         dp[1] = nums[0]
#         maxval = dp[1]
#         for i in range(2, len(nums) + 1):
#             dp[i] = max(dp[:i - 1]) + nums[i - 1]
#             maxval = max(maxval, dp[i])
#         return maxval


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = nums.copy()
        # 1, 2, 3, 1

        for i in range(2, len(nums)):
            if i > 2:
                dp[i] += max(dp[i - 2], dp[i - 3])
            else:
                dp[i] += dp[i - 2]

        return max(dp[-1], dp[-2])


s = Solution()
assert s.rob([1, 2, 3, 1]) == 4
