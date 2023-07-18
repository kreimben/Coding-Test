"""
Ambiguous Measurements
https://www.algoexpert.io/questions/ambiguous-measurements
"""
from functools import lru_cache


def ambiguousMeasurements(cups: [[int]], low: int, high: int):
    cups.sort(reverse=True)

    @lru_cache(maxsize=None)
    def dp(accu_low, accu_high):
        if low <= accu_low <= accu_high <= high:
            return True
        elif accu_low > low or accu_high > high:
            return False

        for l, h in cups:
            res = dp(accu_low + l, accu_high + h)
            if res: return True

        return False

    return dp(0, 0)


assert ambiguousMeasurements([
    [100, 150],
    [1000, 2000]
], 0, 1000) == True
assert ambiguousMeasurements([[10, 20]], 10, 20) == True
assert ambiguousMeasurements([
    [1, 3],
    [2, 4],
    [5, 6]
], 100, 101) == False
assert ambiguousMeasurements([[200, 210]], 10, 20) == False
assert ambiguousMeasurements([[200, 210], [450, 465], [800, 850]], 2100, 2300) == True
