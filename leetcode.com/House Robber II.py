"""
https://leetcode.com/problems/house-robber-ii/
House Robber II
"""
from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)

        @lru_cache(maxsize=None)
        def dp(i: int, limit: int) -> int:
            if i >= limit: return 0
            return max(
                dp(i + 2, limit),
                dp(i + 3, limit)
            ) + nums[i]

        return max(
            dp(0, len(nums) - 1),
            dp(1, len(nums)),
            dp(2, len(nums))
        )


class Solution:
    def rob(self, nums: [int]) -> int:
        # First approach is to get the largest sum with only first element.
        # Second approach is to get the largest sum with only last element.
        onlyFirst = nums[:-1]
        onlyLast = nums[1:]

        def count(array):
            one, two = 0, 0
            for num in array:
                temp = max(num + one, two)
                one = two
                two = temp
            return two

        first = count(onlyFirst)
        second = count(onlyLast)

        return max(first, second, nums[0])


s = Solution()
assert s.rob([1, 2, 3, 1]) == 4
assert s.rob([2, 3, 2]) == 3
