"""
https://leetcode.com/problems/4sum/description/
4Sum
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def count(start, end):  # start index and end index
            nonlocal res
            left, right = start + 1, end - 1

            while left < right:
                # a, b, c and d are distinct.
                ready = [start, left, right, end]
                s = [nums[i] for i in ready]
                if sum(s) == target:
                    if s not in res:
                        res.append(s)
                    left += 1
                elif sum(s) > target:
                    right -= 1
                elif sum(s) < target:
                    left += 1

        for start in range(len(nums) - 3):
            for end in range(start + 3, len(nums)):
                count(start, end)

        return res


s = Solution()
assert s.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
assert s.fourSum([-3, -1, 0, 2, 4, 5], 2) == [[-3, -1, 2, 4]]
assert s.fourSum([-2, -1, -1, 1, 1, 2, 2], 0)
assert s.fourSum([-3, -1, 0, 2, 4, 5], 0) == [[-3, -1, 0, 4]]
