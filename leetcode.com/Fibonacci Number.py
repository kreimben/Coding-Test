"""
https://leetcode.com/problems/fibonacci-number/description/
Fibonacci Number
"""


class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        for i in range(2, n + 1):
            if not memo.get(i, False):
                memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]
