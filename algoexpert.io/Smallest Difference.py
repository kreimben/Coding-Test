"""
https://www.algoexpert.io/questions/smallest-difference
Smallest Difference
"""


def _diff(a: [int]) -> int:
    return a[0] - a[1]


def smallestDifference(one: [int], two: [int]):
    one.sort()  # [-1, 3, 5, 10, 20, 28]
    two.sort()  # [15, 17, 26, 134, 135]

    minimum_difference = [float('-INF'), float('INF')]
    first, second = 0, 0
    while first != len(one) and second != len(two):
        if abs(_diff([one[first], two[second]])) < abs(_diff(minimum_difference)):
            minimum_difference = [one[first], two[second]]

        if one[first] == two[second]:
            return minimum_difference
        elif one[first] > two[second]:
            second += 1
        else:
            first += 1

    return minimum_difference


assert smallestDifference(
    [-1, 5, 10, 20, 28, 3],
    [26, 134, 135, 15, 17]
) == [28, 26]
