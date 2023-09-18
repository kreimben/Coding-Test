"""
Target Sum
https://leetcode.com/problems/target-sum/
"""
from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(i: int, accu: int) -> int:
            if i >= len(nums) - 1: return 1 if accu == target else 0  # return number of cases.
            return dfs(i + 1, accu + nums[i + 1]) + dfs(i + 1, accu - nums[i + 1])

        return dfs(0, nums[0]) + dfs(0, -nums[0])


s = Solution()
assert s.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
