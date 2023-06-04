"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Find First and Last Position of Element in Sorted Array
"""


class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        left, right = 0, len(nums) - 1

        while left <= right:
            if left < len(nums) and target == nums[left] == nums[right]:
                return [left, right]

            if nums[left] < target:
                left += 1
            if target < nums[right]:
                right -= 1

        return [-1, -1]


s = Solution()
assert s.searchRange([2, 2], 3) == [-1, -1]
assert s.searchRange([1], 1) == [0, 0]
assert s.searchRange([1], 0) == [-1, -1]
assert s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
assert s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
