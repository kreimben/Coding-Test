"""
https://leetcode.com/problems/single-number-ii/description/
Single Number II
"""
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = None
        for k, v in c.items():
            if v == 1:
                return k
