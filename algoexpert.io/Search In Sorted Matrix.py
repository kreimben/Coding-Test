"""
https://www.algoexpert.io/questions/search-in-sorted-matrix
Search In Sorted Matrix
"""


def searchInSortedMatrix(matrix: [[int]], target: int):
    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        s = matrix[row][col]

        if s == target:
            return [row, col]
        elif s > target:
            col -= 1
        else:
            row += 1

    return [-1, -1]


assert searchInSortedMatrix([
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
], 32) == [1, 4]

assert searchInSortedMatrix([
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
], 44) == [3, 3]
