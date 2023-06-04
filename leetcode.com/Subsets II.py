"""
https://leetcode.com/problems/subsets-ii/
Subsets II
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sets = [[]]

        for num in nums:
            for i in range(len(sets)):
                ready = sets[i] + [num]
                if ready not in sets:
                    sets.append(ready)

        return sets


s = Solution()
assert s.subsetsWithDup([4, 4, 4, 1, 4]) == [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4],
                                             [4, 4, 4], [4, 4, 4, 4]]
assert s.subsetsWithDup([1, 2, 2]) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
