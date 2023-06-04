"""
https://www.algoexpert.io/questions/min-number-of-coins-for-change
Min Number Of Coins For Change
"""


# def minNumberOfCoinsForChange(n, denoms):
#     dp = [float('inf') for _ in range(n + 1)]
#     dp[0] = 0
#     for denom in denoms:
#         for amount in range(len(dp)):
#             if denom <= amount:
#                 dp[amount] = min(dp[amount], dp[amount - denom] + 1)
#     return dp[n] if dp[n] != float('inf') else -1
def minNumberOfCoinsForChange(target: int, denoms: [int]):
    """
    n: int -> non-negative integer
    """
    denoms = sorted(list(filter(lambda x: x <= target, denoms)))

    dp = [[0 for _ in range(target + 1)] for _ in range(len(denoms))]
    """
    \ 0 1 2 3 4 5 6 7
    1 0 1 2 3 4 5 6 7
    5 0 1 2 3 4 1 2 3 required number of coins
    """
    for di in range(len(denoms)):
        for amount in range(1, target + 1):
            quote = amount // denoms[di]
            if amount >= denoms[di] and quote < denoms[di]:
                dp[di][amount] = quote + dp[di][amount - denoms[di]]
            else:
                dp[di][amount] = dp[di][amount - 1] + 1
    print(f'{dp=}')
    return dp[-1][-1] if dp[-1][-1] else -1


# assert minNumberOfCoinsForChange(7, [1, 5, 10]) == 3
# assert minNumberOfCoinsForChange(7, [3, 7]) == 1
assert minNumberOfCoinsForChange(135, [39, 45, 130, 40, 4, 1, 60, 75]) == 2
