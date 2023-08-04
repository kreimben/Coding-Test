"""
Rotate Image
https://leetcode.com/problems/rotate-image/description/
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # make values in a row (1D array)
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr.append(matrix[i][j])

        index = 0
        for j in range(len(matrix) - 1, -1, -1):
            for i in range(len(matrix[0])):
                matrix[i][j] = arr[index]
                index += 1
