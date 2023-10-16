"""
https://leetcode.com/problems/maximum-subarray/
Maximum Subarray
"""


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        minval, maxval = 0, 0
        res = max(nums)

        for num in nums:
            mintemp, maxtemp = minval + num, maxval + num

            minval = min(mintemp, maxtemp, num)
            maxval = max(mintemp, maxtemp, num)

            res = max(res, maxval)

        return res
