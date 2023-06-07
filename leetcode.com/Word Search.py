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

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#
#         R = len(board)
#         C = len(board[0])
#
#         if len(word) > R * C:
#             return False
#
#         count = Counter(sum(board, []))
#
#         for c, countWord in Counter(word).items():
#             if count[c] < countWord:
#                 return False
#
#         if count[word[0]] > count[word[-1]]:
#             word = word[::-1]
#
#         seen = set()
#
#         def dfs(r, c, i):
#             if i == len(word):
#                 return True
#             if r < 0 or c < 0 or r >= R or c >= C or word[i] != board[r][c] or (r, c) in seen:
#                 return False
#
#             seen.add((r, c))
#             res = (
#                     dfs(r + 1, c, i + 1) or
#                     dfs(r - 1, c, i + 1) or
#                     dfs(r, c + 1, i + 1) or
#                     dfs(r, c - 1, i + 1)
#             )
#             seen.remove((r, c))  # backtracking
#
#             return res
#
#         for i in range(R):
#             for j in range(C):
#                 if dfs(i, j, 0):
#                     return True
#         return False
