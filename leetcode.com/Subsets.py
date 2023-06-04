"""
https://leetcode.com/problems/subsets/
Zigzag Conversion
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


s = Solution()
actual = s.subsets([1, 2, 3])
expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
assert actual == expected
