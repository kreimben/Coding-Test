"""
Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(i, j, visit, prev):
            nonlocal ROWS, COLS
            if (i, j) in visit or not (0 <= i < ROWS and 0 <= j < COLS) or heights[i][j] < prev:
                return
            visit.add((i, j))
            dfs(i + 1, j, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))

        return res

# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         N, M = len(heights), len(heights[0])
#         res = [(0, M - 1), (N - 1, 0)]
#
#         @lru_cache(maxsize=None)
#         def is_valid(x: int, y: int) -> bool:
#             return 0 <= x < len(heights) and 0 <= y < len(heights[0])
#
#         @lru_cache(maxsize=None)
#         def dfs(x: int, y: int) -> bool:
#             nonlocal res, N, M
#             if x == 0 or y == 0 or x == N - 1 or y == M - 1:
#                 return True
#             else:
#                 if is_valid(x, y):
#                     if (heights[x - 1][y] <= heights[x][y] or \
#                         heights[x][y - 1] <= heights[x][y]) and \
#                             (heights[x + 1][y] <= heights[x][y] or \
#                              heights[x][y + 1] <= heights[x][y]):
#                         res.append((x, y))
#                         return (dfs(x - 1, y) or dfs(x, y - 1)) and (dfs(x + 1, y) or dfs(x, y + 1))
#
#             return False
#
#         dfs(*res[0])
#
#         return list(set(res))
