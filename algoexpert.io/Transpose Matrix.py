"""
https://www.algoexpert.io/questions/transpose-matrix
Transpose Matrix
"""


def transposeMatrix(matrix):
    res = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            res[i][j] = matrix[j][i]
    return res
