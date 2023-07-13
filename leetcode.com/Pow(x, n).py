"""
https://leetcode.com/problems/powx-n/description/
Pow(x, n)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1 / pow(x, -n)
        return x * pow(x, n - 1)
