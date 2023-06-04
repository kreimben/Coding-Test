"""
https://www.algoexpert.io/questions/four-number-sum
Four Number Sum
"""


def fourNumberSum(array, targetSum):
    array.sort()
    res = []

    def count(start, end):
        nonlocal res
        left, right = start + 1, end - 1
        while left < right:
            ready = [start, left, right, end]
            s = [array[i] for i in ready]
            if sum(s) == targetSum:
                if s not in res:
                    res.append(s)
                left += 1
            elif sum(s) > targetSum:
                right -= 1
            elif sum(s) < targetSum:
                left += 1

    for start in range(len(array) - 3):
        for end in range(start + 3, len(array)):
            count(start, end)
    return res


assert sorted(fourNumberSum([5, -5, -2, 2, 3, -3], 0)) == sorted([
    sorted([5, -5, -2, 2]),
    sorted([5, -5, 3, -3]),
    sorted([-2, 2, 3, -3])
])
assert sorted(fourNumberSum([1, 2, 3, 4, 5, 6, 7], 10)) == sorted([
    [1, 2, 3, 4]
])
assert sorted(fourNumberSum([1, 2, 3, 4, 5, -5, 6, -6], 5)) == sorted([
    sorted([2, 3, 5, -5]),
    sorted([1, 4, 5, -5]),
    sorted([2, 4, 5, -6]),
    sorted([1, 3, -5, 6]),
    sorted([2, 3, 6, -6]),
    sorted([1, 4, 6, -6])
])
assert sorted(fourNumberSum([7, 6, 4, -1, 1, 2], 16)) == sorted([
    sorted([7, 6, 4, -1]),
    sorted([7, 6, 1, 2])
])
