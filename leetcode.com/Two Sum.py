"""
https://leetcode.com/problems/two-sum/
Two Sum
"""
from typing import List


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            d[target - num] = i

        for wanted, target_index in d.items():
            if wanted in nums:
                wanted_index = nums.index(wanted)
                if target_index != wanted_index:
                    return sorted([target_index, wanted_index])


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            if target - num in nums and (index := nums.index(target - num)) != i:
                return sorted([i, index])


s = Solution()

assert s.twoSum([-3, 4, 3, 90], 0) == [0, 2]
assert s.twoSum([2, 3, 4], 6) == [0, 2]
assert s.twoSum([3, 3], 6) == [0, 1]
assert s.twoSum([0, 4, 3, 0], 0) == [0, 3]
assert s.twoSum([-3, 4, 3, 90], 0) == [0, 2]
