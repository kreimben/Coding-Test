"""
https://www.algoexpert.io/questions/sorted-squared-array
Sorted Squared Array
"""


def sortedSquaredArray(array: [int]):
    result = [x * x for x in array]
    result.sort()
    return result


assert sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]) == [1, 4, 9, 25, 36, 64, 81]
