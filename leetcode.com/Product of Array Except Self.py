"""
https://leetcode.com/problems/product-of-array-except-self/
Product of Array Except Self
"""
from collections import defaultdict


class Solution:
    prefix = defaultdict(int)
    postfix = defaultdict(int)

    def count_prefix(self, index: int, last_num: int):
        self.prefix[index] = self.prefix[index - 1] * last_num

    def count_postfix(self, index: int, first_num: int):
        self.postfix[index] = self.postfix[index + 1] * first_num

    def calculate(self, index: int) -> int:
        result = self.prefix[index - 1] * self.postfix[index + 1]
        return result

    def productExceptSelf(self, nums: [int]) -> [int]:
        results = []
        self.prefix[-1] = 1
        self.postfix[len(nums)] = 1

        for i in range(len(nums)):
            self.count_prefix(i, nums[i])
            self.count_postfix(len(nums) - 1 - i, nums[len(nums) - 1 - i])

        for i in range(len(nums)):
            r = self.calculate(i)
            results.append(r)

        return results


s = Solution()
assert s.productExceptSelf([0, 0]) == [0, 0]
assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
