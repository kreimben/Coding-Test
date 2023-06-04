"""
https://leetcode.com/problems/maximum-subarray/
Maximum Subarray
"""


# class Solution:
#     def maxSubArray(self, nums) -> int:
#         # subarray must be contiguous in parent array.
#         # subarray's size is free but must not be empty.
#         pre = {}
#         post = {}
#         total = sum(nums)
#
#         nums = [(i, num) for i, num in enumerate(nums)]
#
#         for i, num in nums:
#             pre[i] = num + pre.get(i - 1, 0)
#
#         for i, num in reversed(nums):
#             post[i] = num + post.get(i + 1, 0)
#
#         most = float('-inf')
#         for i in range(-1, len(nums) - 1):
#             for j in range(i + 2, len(nums) + 1):
#                 curr = total - pre.get(i, 0) - post.get(j, 0)
#                 most = max(
#                     most,
#                     curr
#                 )
#
#         return most

class Solution:
    """
    유명한 풀이
    """

    def maxSubArray(self, nums: [int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum


s = Solution()
assert s.maxSubArray([-1]) == -1
assert s.maxSubArray([1]) == 1
assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
