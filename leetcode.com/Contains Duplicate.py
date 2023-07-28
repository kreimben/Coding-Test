"""
Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if d.get(num, False):
                return True
            else:
                d[num] = True
        return False
