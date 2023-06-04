"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
Search in Rotated Sorted Array
"""


class Solution:
    def search(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right

            if nums[mid] > nums[-1]:
                # pivot should be right of mid.
                # and nums array is rotated.
                if nums[left] <= target <= nums[mid]:
                    # If target supposed to be left department using pivot.
                    # Make right should be mid.
                    right = mid if right != mid else left - 1
                elif nums[mid] <= target <= nums[right]:
                    # If target supposed to be right department using pivot.
                    left = mid if left != mid else right + 1
                else:
                    # If not found range => mid should be expanded to right.
                    left += 1
            else:
                # In this case, nums array is completly sorted.
                # So adjust with normal binary search.
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right -= 1
                elif nums[mid] < target:
                    left += 1
        return -1


s = Solution()
assert s.search([3, 5, 1], 5) == 1
assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert s.search([4, 5, 6, 7, 0, 1, 2], 1) == 5
assert s.search([1], 1) == 0
assert s.search([3, 1], 3) == 0
assert s.search([3, 1], 0) == -1
assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
