"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Find Minimum in Rotated Sorted Array
"""
from typing import List


class Solution:
    def findMin(self, nums: [int]) -> int:
        left, right = 0, len(nums) - 1
        curr_min = float('inf')

        while left < right:
            mid = (left + right) // 2
            curr_min = min(curr_min, nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return min(curr_min, nums[left])


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:
                # it's neutral.
                if left == 0 or nums[left - 1] > nums[left]:
                    return nums[left]
                else:
                    left -= 1
            else:
                # if it's rotated and not neutral.
                left = (left + right) // 2 + 1


s = Solution()
assert s.findMin([5, 1, 2, 3, 4]) == 1
assert s.findMin([3, 1, 2]) == 1
assert s.findMin([1, 2]) == 1
assert s.findMin([2, 1]) == 1
assert s.findMin([11, 13, 15, 17]) == 11
assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert s.findMin([3, 4, 5, 1, 2]) == 1
