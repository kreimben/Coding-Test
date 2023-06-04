"""
https://leetcode.com/problems/binary-search/
Binary Search
"""


class Solution:
    def search(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if left > right:
            return -1


s = Solution()
assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
