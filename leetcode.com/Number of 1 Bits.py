"""
https://leetcode.com/problems/number-of-1-bits/description/
Number of 1 Bits
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        s = list(bin(n)[2:])
        count = 0
        for ch in s:
            if ch == '1':
                count += 1
        return count
