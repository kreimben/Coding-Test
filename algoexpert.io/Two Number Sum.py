"""
https://www.algoexpert.io/questions/two-number-sum
Two Number Sum
"""
from collections import defaultdict


def twoNumberSum(array: [int], targetSum: int):
    results = defaultdict(int)

    for num in array:
        results[targetSum - num] += 1

    keys = results.keys()

    for i, num in enumerate(keys):
        if num in array and num != array[i]:
            # print(f'I found the very that numer!: {array[i]=} {num=}')
            return [num, array[i]]

    return []


assert (twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11])
