"""
https://leetcode.com/problems/word-search/
Word Search
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # length check
        if len(word) > len(board) * len(board[0]): return False

        # non-existing element check
        s = set()
        for arr in board:
            for ch in arr:
                s.add(ch)
        for ch in word:
            if ch not in s: return False

        # DFS
        visited = set()

        def dfs(x, y, i) -> bool:
            nonlocal visited
            case = (
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)
            )

            if i == len(word):
                return True
            elif not (0 <= x < len(board) and 0 <= y < len(board[0])) or \
                    board[x][y] != word[i] or \
                    (x, y) in visited:
                return False

            visited.add((x, y))
            res = [
                dfs(x + 1, y, i + 1),
                dfs(x - 1, y, i + 1),
                dfs(x, y + 1, i + 1),
                dfs(x, y - 1, i + 1)
            ]
            visited.remove((x, y))

            return any(res)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         # check first
#         s = set()
#         for arr in board:
#             for ch in arr:
#                 s.add(ch)
#         for ch in word:
#             if ch not in s: return False
#
#         # find it
#         case = (
#             (0, 1),
#             (0, -1),
#             (1, 0),
#             (-1, 0)
#         )
#
#         def is_valid(x: int, y: int) -> bool:
#             return 0 <= x < len(board) and \
#                 0 <= y < len(board[0])
#
#         stack = []
#
#         def combination() -> str:
#             nonlocal stack
#             res = ''
#             for x, y in stack:
#                 res += board[x][y]
#             return res
#
#         def search(i: int, j: int, index: int):
#             nonlocal case, stack
#             if combination() == word:
#                 return True
#             elif len(stack) >= len(word):
#                 return False
#
#             for di, dj in case:
#                 x = i + di
#                 y = j + dj
#                 if is_valid(x, y) and \
#                         word[index + 1] == board[x][y] and \
#                         (x, y) not in stack:
#
#                     stack.append((x, y))
#                     res = search(x, y, index + 1)
#                     stack.pop()
#                     if res: return True
#
#             return False
#
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     stack.append((i, j))
#                     res = search(i, j, 0)
#                     stack.pop()
#                     if res:
#                         return True
#
#         return False


s = Solution()
assert s.exist([["a", "a"]], "aaa") == False

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         N = len(word)
#         res = []
#         case = [
#             (0, 1),
#             (1, 0),
#             (-1, 0),
#             (0, -1)
#         ]
#
#         def dfs(s: [Tuple[int, int]]):
#             nonlocal N
#             if len(s) == N:
#                 res.append(s)
#                 return
#             # generate four case.
#             curr = s[-1]
#             for di, dj in case:
#                 x = curr[0] + di
#                 y = curr[1] + dj
#
#                 # if x and y is in valid range.
#                 if (0 <= x < len(board)) and \
#                         (0 <= y < len(board[0])) and \
#                         word[len(s)] == board[x][y] and \
#                         (x, y) not in s:
#                     dfs(s + [(x, y)])
#
#         # can start from anywhere.
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 # but should check if initial char is same with curr point.
#                 if board[i][j] == word[0]:
#                     dfs([(i, j)])
#
#         if res:
#             return True
#         else:
#             return False

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
