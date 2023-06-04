"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Two Sum II - Input Array Is Sorted
"""


class Solution:

    def twoSum(self, numbers: [int], target: int) -> [int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            else:
                left += 1

            if left == right:
                right += 1


s = Solution()
assert s.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
assert s.twoSum([0, 0, 3, 4], 0) == [1, 2]
assert s.twoSum([2, 3, 4], 6) == [1, 3]
assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
