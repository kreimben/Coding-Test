"""
https://www.algoexpert.io/questions/monotonic-array
Monotonic Array
"""


def isMonotonic(array: [int]):
    if not array:
        return True

    # Just compare first and end of array.
    is_increasing = True if array[0] < array[len(array) - 1] else False

    for i in range(len(array) - 1):
        first = array[i]
        second = array[i + 1]

        if (is_increasing and first > second) or (not is_increasing and first < second):
            return False

    return True
