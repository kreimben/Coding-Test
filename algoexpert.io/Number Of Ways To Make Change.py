"""
https://www.algoexpert.io/questions/number-of-ways-to-make-change
Number Of Ways To Make Change
"""


def numberOfWaysToMakeChange(n, denoms):  # n is target number for combinations of denominations.
    denoms = list(filter(lambda x: x <= n, denoms))  # filter that we can't use cuz of bigger than n.
    ways = [0] * (n + 1)
    ways[0] = 1  # nothing with 0 target number always meets one case.

    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]


assert numberOfWaysToMakeChange(10, [1, 5, 10, 25]) == 4
assert numberOfWaysToMakeChange(6, [1, 5]) == 2
