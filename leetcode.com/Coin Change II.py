"""
https://leetcode.com/problems/coin-change-ii/
Coin Change II
"""
from functools import cache
from typing import List


class Solution:
    """
    cached dfs.
    """

    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def dfs(before: int, rest: int):
            if rest == 0:
                return 1  # means 1 case.
            case = 0
            for coin in coins:
                if coin <= before and rest >= coin:
                    case += dfs(coin, rest - coin)
            return case

        return dfs(max(coins), amount)

# class Solution:
#     """
#     The very basic form of backtracking.
#     backtracking is slow to pass all test cases.
#     """
#
#     def change(self, amount: int, coins: List[int]) -> int:
#         case = set()
#         arr = []
#
#         def backtracking():
#             nonlocal case, arr
#             if sum(arr) == amount:
#                 case.add(tuple(sorted(arr)))
#                 return
#             elif sum(arr) > amount:
#                 return
#
#             for denom in coins:
#                 arr.append(denom)
#                 backtracking()
#                 arr.pop()
#
#         backtracking()
#
#         return len(case)
