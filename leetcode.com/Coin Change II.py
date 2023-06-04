"""
https://leetcode.com/problems/coin-change-ii/
Coin Change II
"""
from typing import List


class Solution:
    """
    The very basic form of backtracking.
    """

    def change(self, amount: int, coins: List[int]) -> int:
        case = set()
        arr = []

        def backtracking():
            nonlocal case, arr
            if sum(arr) == amount:
                case.add(tuple(sorted(arr)))
                return
            elif sum(arr) > amount:
                return

            for denom in coins:
                arr.append(denom)
                backtracking()
                arr.pop()

        backtracking()

        return len(case)
