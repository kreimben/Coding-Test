"""
https://leetcode.com/problems/word-search/
Word Search
"""
from typing import Tuple, List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(word)
        res = []
        case = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]

        def dfs(s: [Tuple[int, int]]):
            nonlocal N
            if len(s) == N:
                res.append(s)
                return
            # generate four case.
            curr = s[-1]
            for di, dj in case:
                x = curr[0] + di
                y = curr[1] + dj

                # if x and y is in valid range.
                if (0 <= x < len(board)) and \
                        (0 <= y < len(board[0])) and \
                        word[len(s)] == board[x][y] and \
                        (x, y) not in s:
                    dfs(s + [(x, y)])

        # can start from anywhere.
        for i in range(len(board)):
            for j in range(len(board[0])):
                # but should check if initial char is same with curr point.
                if board[i][j] == word[0]:
                    dfs([(i, j)])

        if res:
            return True
        else:
            return False
