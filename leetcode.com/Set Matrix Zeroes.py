"""
https://leetcode.com/problems/set-matrix-zeroes/description/
Set Matrix Zeroes
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        stack = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    stack.append((i, j))

        while stack:
            i, j = stack.pop()
            # e.i) 0, 0 => x, 0 and 0, y
            for x in range(len(matrix[0])):
                matrix[i][x] = 0

            for y in range(len(matrix)):
                matrix[y][j] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Must find where is 0
        x, y = [], []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    y.append(i)
                    x.append(j)

        for i in range(len(matrix)):
            # during scanning up to down, use x array.
            for col in x:
                matrix[i][col] = 0

        for j in range(len(matrix[0])):
            # during scanning left to right, use y array.
            for row in y:
                matrix[row][j] = 0
