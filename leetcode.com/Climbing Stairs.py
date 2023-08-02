"""
https://leetcode.com/problems/climbing-stairs/
Climbing Stairs
"""
from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):  # 1 ~ n
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[len(dp) - 1]


class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(step: int) -> int:
            if step < 3:
                return step
            return dp(step - 1) + dp(step - 2)

        return dp(n)


s = Solution()
assert s.climbStairs(2) == 2
assert s.climbStairs(3) == 3
