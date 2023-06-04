"""
https://leetcode.com/problems/minimum-size-subarray-sum/
Minimum Size Subarray Sum
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: [int]):
        start, res = 0, len(nums) + 1
        for end in range(len(nums)):
            target -= nums[end]
            while target <= 0:
                res = min(res, end - start + 1)
                target += nums[start]
                start += 1
        return res % (len(nums) + 1)


s = Solution()
assert s.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3
assert s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
assert s.minSubArrayLen(4, [1, 4, 4]) == 1
assert s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
