"""
https://leetcode.com/problems/valid-sudoku/
Valid Sudoku
"""
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        # First, I should check each row.
        for i in range(9):
            d = defaultdict(int)
            for j in range(9):
                if board[i][j] != '.' and d[board[i][j]] > 0:
                    return False
                else:
                    d[board[i][j]] += 1
        del d, i
        # Second, I should check each column.
        for i in range(9):
            d = defaultdict(int)
            for j in range(9):
                if board[j][i] != '.' and d[board[j][i]] > 0:
                    return False
                else:
                    d[board[j][i]] += 1
        del d, i
        # Third, I should check each of the nine sub-boxes of the grid.
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # Nested O(n^2)
                d = defaultdict(int)
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        b = board[ii][jj]
                        if b != '.' and d[b] > 0:
                            return False
                        else:
                            d[board[ii][jj]] += 1

        return True


s = Solution()

board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]
assert s.isValidSudoku(board) == False
