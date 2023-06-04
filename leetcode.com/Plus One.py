"""
https://leetcode.com/problems/plus-one/description/
Plus One
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join([str(digit) for digit in digits])
        s = int(s)
        s += 1
        return [int(digit) for digit in str(s)]
