"""
https://leetcode.com/problems/counting-bits/description/
Counting Bits
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(s: str):
            c = 0
            for ch in s:
                if ch == '1':
                    c += 1
            return c

        return [count(bin(i)[2:]) for i in range(n + 1)]
