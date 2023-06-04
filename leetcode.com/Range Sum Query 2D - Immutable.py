"""
https://leetcode.com/problems/range-sum-query-2d-immutable/
Range Sum Query 2D - Immutable
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.saved = {}  # defaultdict(int)
        # It's okay to save accumulated values in O(n^2).
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # add accumulated value.
                for x in range(i + 1):
                    for y in range(j + 1):
                        self.saved[(i, j)] += matrix[x][y]  # self.saved[(x, y)]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.saved[(row2, col2)]
        # first range
        ran_i, ran_j = row1 - 1, col2
        if 0 <= ran_i < self.rows and 0 <= ran_j < self.cols:
            res -= self.saved[(ran_i, ran_j)]

        # second range
        ran_i, ran_j = row2, col1 - 1
        if 0 <= ran_i < self.rows and 0 <= ran_j < self.cols:
            res -= self.saved[(ran_i, ran_j)]

        # third range
        ran_i, ran_j = row1 - 1, col1 - 1
        if 0 <= ran_i < self.rows and 0 <= ran_j < self.cols:
            res += self.saved[(ran_i, ran_j)]

        return res


commands = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
inputs = [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3],
          [1, 1, 2, 2], [1, 2, 2, 4]]
res = []
expected = [None, 8, 11, 12]
s = None

for command, input, exptect in list(zip(commands, inputs, expected)):
    if command == 'NumMatrix':
        s = NumMatrix(input[0])
    elif command == 'sumRegion':
        assert exptect == s.sumRegion(*input)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
