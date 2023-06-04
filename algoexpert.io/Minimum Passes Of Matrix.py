"""
https://www.algoexpert.io/questions/minimum-passes-of-matrix
Minimum Passes Of Matrix
"""
from copy import deepcopy


def minimumPassesOfMatrix(matrix):
    case = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]
    count = 0
    while True:
        temp = deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] >= 0:  # we don't need a positive number or 0
                    continue  # We only find negative numbers.
                for ai, aj in case:
                    ci, cj = i + ai, j + aj

                    if 0 <= ci < len(matrix) and 0 <= cj < len(matrix[0]) and matrix[ci][cj] > 0:
                        temp[i][j] = -temp[i][j]  # Make that positive!
                        break  # The once is enough!
        count += 1
        if matrix != temp:
            matrix = temp
        else:
            # Check that if I can convert negative numbers
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] < 0:
                        return -1
            else:
                break
    return count - 1


assert minimumPassesOfMatrix([
    [1, 0, 0, -2, -3],
    [-4, -5, -6, -2, -1],
    [0, 0, 0, 0, -1],
    [-1, 0, 3, 0, 3]
]) == -1
assert minimumPassesOfMatrix([
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
]) == 3
