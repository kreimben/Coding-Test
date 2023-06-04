"""
https://leetcode.com/problems/house-robber-ii/
House Robber II
"""


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
