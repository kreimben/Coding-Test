"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Best Time to Buy and Sell Stock
"""


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            sell += 1

        return max_profit


s = Solution()
assert s.maxProfit([2, 4, 1]) == 2
assert s.maxProfit([7, 6, 4, 3, 1]) == 0
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
