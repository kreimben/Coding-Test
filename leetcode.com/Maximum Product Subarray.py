"""
not solved.
https://leetcode.com/problems/maximum-product-subarray/
Maximum Product Subarray
"""


def product(args: [int]):
    result = 1
    for arg in args:
        result *= arg
    return result


class Solution:

    def maxProduct(self, nums: [int]) -> int:
        if min(nums) > 0:
            return product(nums)  # In this case, Every element is positive.
        elif max(nums) < 0:
            # In this case, Every element is negative.
            nums.remove(max(nums))
            return product(nums)

        # And the rest...
        # Just find where is the first positive index.
        left = 0
        maximum = float('-inf')
        for i, v in enumerate(nums):
            if v > 0:
                left = i

        negative_index = []
        for i in range(len(nums)):
            if nums[i] < 0:
                negative_index.append(i)
        right = negative_index[0]

        while right < negative_index[len(negative_index) - 1]:
            maximum = max(maximum, product(nums[left:right]))

            # Find next left and right index.
            for i in range(1, len(negative_index)):
                right = negative_index[i]


s = Solution()
# assert s.maxProduct([-4, -3]) == 12
# assert s.maxProduct([-2]) == -2
assert s.maxProduct([2, 3, -2, 4]) == 6
assert s.maxProduct([-2, 0, -1]) == 0
