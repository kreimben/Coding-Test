"""
https://leetcode.com/problems/surrounded-regions/
Surrounded Regions
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        # 테두리의 'O'를 찾는다.
        borders = []
        for i in range(len(board)):
            borders.append((i, 0))
            borders.append((i, len(board[0]) - 1))
        for j in range(len(board[0])):
            borders.append((0, j))
            borders.append((len(board) - 1, j))

        # DFS를 사용하여 테두리 'O'와 연결된 'O'를 찾는다.
        while borders:
            i, j = borders.pop()
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
                board[i][j] = 'T'
                borders.append((i + 1, j))
                borders.append((i - 1, j))
                borders.append((i, j + 1))
                borders.append((i, j - 1))

        # 'O'를 'X'로, 'T'를 'O'로 바꾼다.
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'


s = Solution()
given = [
    ["O", "X", "X", "O", "X"],
    ["X", "O", "O", "X", "O"],
    ["X", "O", "X", "O", "X"],
    ["O", "X", "O", "O", "O"],
    ["X", "X", "O", "X", "O"]
]
expected = [
    ["O", "X", "X", "O", "X"],
    ["X", "X", "X", "X", "O"],
    ["X", "X", "X", "O", "X"],
    ["O", "X", "O", "O", "O"],
    ["X", "X", "O", "X", "O"]
]
s.solve(given)

assert given == expected

given = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
expected = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
s.solve(given)

assert given == expected
