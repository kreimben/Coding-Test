"""
Find Peak Element
https://leetcode.com/problems/find-peak-element/description/
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Binary Search Solution
        Time complexity: O(log n)
        Space complexity: O(1)
        """

        def search(left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return search(left, mid)
            else:
                return search(mid + 1, right)

        return search(0, len(nums) - 1)
