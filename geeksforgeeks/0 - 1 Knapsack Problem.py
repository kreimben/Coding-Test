"""
0 - 1 Knapsack Problem
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
"""

# User function Template for python3
from functools import lru_cache


class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, maximum_weight: int, weights: [int], values: [int], n: int):
        # `n` is just number of items, so equivalent of len(weights) and len(values).

        @lru_cache(maxsize=None)
        def select(index: int, weight: int) -> int:
            if index >= n or weight >= maximum_weight: return 0  # maximum value of selected items.

            maxval = 0
            for i in range(index + 1, n):
                if weights[i] + weight <= maximum_weight:
                    maxval = max(maxval, select(i, weight + weights[i]) + values[i])

            return maxval

        maxval = 0
        for i in range(n):
            if weights[i] <= maximum_weight:
                maxval = max(maxval, select(i, weights[i]) + values[i])

        return maxval
