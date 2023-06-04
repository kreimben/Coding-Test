"""
https://www.algoexpert.io/questions/non-constructible-change
Non-Constructible Change
"""
from itertools import combinations


def check_target(arr: [int], target_number: int) -> bool:
    for i in range(2, len(arr) + 1):
        for subset in combinations(arr, i):
            sum = 0
            for ele in subset:
                sum += ele
            if target_number == sum:
                return True
    return False


def nonConstructibleChange(coins: [int]):
    """
    It's Big-O notation is O(n^4). What a terrible.
    """
    minimum_target = 1

    if not len(coins):
        return minimum_target

    coins.sort()

    while True:
        # First, We should find target number directly in array(`coins`).
        if minimum_target not in coins:
            # If not in array(`coins`), We should combine the numbers.
            if not check_target(coins.copy(), minimum_target):
                return minimum_target

        minimum_target += 1


assert nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]) == 20
