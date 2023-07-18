"""
Maximize Expression
https://www.algoexpert.io/questions/maximize-expression
"""

import math


def maximizeExpression(array):
    N = len(array)
    if N < 4:
        return 0

    dp = [[-math.inf] * N for _ in range(4)]

    row = 0

    # A
    for i, num in enumerate(array):
        dp[row][i] = max(dp[row][i - 1], array[i])

    # A - B
    row = 1
    for i, num in enumerate(array):
        if i < 1:
            continue
        dp[row][i] = max(
            dp[row - 1][i - 1] - array[i],
            dp[row][i - 1]
        )

    # A - B + C
    row = 2
    for i, num in enumerate(array):
        if i < 2:
            continue
        dp[row][i] = max(
            dp[row - 1][i - 1] + array[i],
            dp[row][i - 1]
        )

    # A - B + C - D
    row = 3
    for i, num in enumerate(array):
        if i < 2:
            continue
        dp[row][i] = max(
            dp[row - 1][i - 1] - array[i],
            dp[row][i - 1]
        )

    return dp[-1][-1]

# def maximizeExpression(array):
#     """
#     initial solution
#     """
#     if len(array) < 4:
#         return 0
#
#     def dp(i: int, level: int):
#         if level == 4:
#             return 0
#
#         maxval = -math.inf
#         for next_index in range(i + 1, len(array)):
#             if level % 2 == 0:
#                 next_target = array[next_index]
#             else:
#                 next_target = -array[next_index]
#             maxval = max(maxval, dp(next_index, level + 1) + next_target)
#         return maxval
#
#     maxval = -math.inf
#     for i in range(len(array)):
#         maxval = max(maxval, dp(i, 1) + array[i])
#
#     return maxval
