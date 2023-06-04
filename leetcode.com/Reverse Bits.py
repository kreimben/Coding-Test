"""
https://leetcode.com/problems/reverse-bits/description/
Reverse Bits
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:][::-1]
        if len(s) < 32:
            s += ''.join(['0' for _ in range(32 - len(s))])
        return int(s, 2)
