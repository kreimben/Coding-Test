"""
https://leetcode.com/problems/maximum-product-subarray/
Maximum Product Subarray
"""


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        maxval = 0
        res = max(nums)

        for num in nums:
            maxval = max(maxval + num, num)

            res = max(res, maxval)

        return res


import math


class Solution:
    def neg(self, arr) -> int:
        count = 0
        for num in arr:
            if num < 0: count += 1
        return count

    def product(self, arr) -> int:
        count = 1
        for num in arr:
            count *= num
        return count

    def maxProduct(self, nums: [int]) -> int:
        if not nums: return -math.inf
        maxval = min(nums)
        if self.neg(nums) % 2 == 0:
            maxval = max(maxval, self.product(nums))

        return max(
            maxval,
            self.maxProduct(nums[1:]),
            self.maxProduct(nums[:-1])
        )


# def product(args: [int]):
#     result = 1
#     for arg in args:
#         result *= arg
#     return result
#
#
# class Solution:
#
#     def maxProduct(self, nums: [int]) -> int:
#         if min(nums) > 0:
#             return product(nums)  # In this case, Every element is positive.
#         elif max(nums) < 0:
#             # In this case, Every element is negative.
#             nums.remove(max(nums))
#             return product(nums)
#
#         # And the rest...
#         # Just find where is the first positive index.
#         left = 0
#         maximum = float('-inf')
#         for i, v in enumerate(nums):
#             if v > 0:
#                 left = i
#
#         negative_index = []
#         for i in range(len(nums)):
#             if nums[i] < 0:
#                 negative_index.append(i)
#         right = negative_index[0]
#
#         while right < negative_index[len(negative_index) - 1]:
#             maximum = max(maximum, product(nums[left:right]))
#
#             # Find next left and right index.
#             for i in range(1, len(negative_index)):
#                 right = negative_index[i]


s = Solution()
assert s.maxProduct([-3, 0, 1, -2]) == 1
assert s.maxProduct([-4, -3]) == 12
assert s.maxProduct([-2]) == -2
assert s.maxProduct([2, 3, -2, 4]) == 6
assert s.maxProduct([-2, 0, -1]) == 0
