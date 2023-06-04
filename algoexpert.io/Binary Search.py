"""
https://www.algoexpert.io/questions/binary-search
Binary Search
"""


def binarySearch(array: [int], target: int):
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if target > array[mid]:
            left += 1
        elif target < array[mid]:
            right -= 1
        else:
            return mid
    return -1


assert binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33) == 3
assert binarySearch([1, 5, 23, 111], 120) == -1
