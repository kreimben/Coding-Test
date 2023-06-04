"""
https://www.algoexpert.io/questions/subarray-sort
Subarray Sort
"""


def subarraySort(array):
    s = sorted(array)
    if s == array:
        return [-1, -1]
    # I will use binary search. From starting index to ending index.
    # During binary search, left side of left index could be decreasing.
    # the right side of right index could be increasing.
    left, right = 0, len(array) - 1
    while left < right:
        moved = False
        if s[left] == array[left]:
            left += 1
            moved = True
        if s[right] == array[right]:
            right -= 1
            moved = True

        if not moved:
            break

    return [left, right]


assert subarraySort([1, 2]) == [-1, -1]
assert subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]) == [3, 9]
