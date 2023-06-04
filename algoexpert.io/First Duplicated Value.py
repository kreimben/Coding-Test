"""
https://www.algoexpert.io/questions/first-duplicate-value
First Duplicated Value
"""


def firstDuplicateValue(nums: [int]):
    # Solution should be O(n)
    d = {}
    for num in nums:
        if d.get(num) is not None:
            return num
        else:
            d[num] = 1
    return -1


assert firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]) == 2
