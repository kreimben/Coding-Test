"""
https://leetcode.com/problems/find-the-duplicate-number/description/
Find the Duplicate Number
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if d.get(num, False):
                return num
            else:
                d[num] = True
