"""
https://leetcode.com/problems/coin-change/description/
Coin Change
"""
import math
from functools import lru_cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        @lru_cache(maxsize=None)
        def dfs(rest: int) -> int:
            if rest == 0:
                return 0
            elif rest < 0:
                return math.inf

            temp = math.inf
            for coin in coins:
                res = dfs(rest - coin) + 1
                temp = min(temp, res)

            return temp

        res = dfs(amount)
        return res if res != math.inf else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for amount in range(len(dp)):
                if coin <= amount:
                    dp[amount] = min(dp[amount], dp[amount - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


s = Solution()
# assert s.coinChange([411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864) == 24
assert s.coinChange([1, 2, 5], 11) == 3
