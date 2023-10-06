"""
https://leetcode.com/problems/missing-number/description/
Missing Number
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res


class Solution:
    """
    it's not O(1) space complexity
    """

    def missingNumber(self, nums: List[int]) -> int:
        maxnum = max(len(nums), max(nums))
        check = [0] * (maxnum + 1)
        for i in range(maxnum + 1):
            if i in nums:
                check[i] = 1
        return check.index(0)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = max(max(nums), len(nums))
        total = sum([i for i in range(N + 1)])
        return total - sum(nums)
