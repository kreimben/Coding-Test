"""
https://www.algoexpert.io/questions/search-for-range
Search For Range
"""


def searchForRange(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (right + left) // 2
        if array[mid] == target:
            # Start from there.
            # Spread the range of target number.
            left, right = mid, mid
            while left > -1 and array[left] == target:
                left -= 1
            while len(array) > right and array[right] == target:
                right += 1
            return [left + 1, right - 1]
        elif array[mid] > target:
            right -= 1
        elif array[mid] < target:
            left += 1
    else:
        return [-1, -1]


assert searchForRange([5, 7, 7, 8, 8, 10], 10) == [5, 5]
assert searchForRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45) == [4, 9]
