"""
https://leetcode.com/problems/coin-change/description/
Coin Change
"""
from typing import List


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
assert s.coinChange([1, 2, 5], 11) == 3
