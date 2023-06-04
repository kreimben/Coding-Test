"""
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/
Maximum Number of Moves in a Grid
"""
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        maxval = 0  # maximum number of moves.
        visited = set()

        # go with DFS.
        def dfs(i, j, count):
            nonlocal maxval
            if (i, j) in visited:
                return
            else:
                visited.add((i, j))

            if j >= len(grid[0]) - 1:
                # we are reached to boundary!
                maxval = max(maxval, count)
                return
            else:
                temp = []
                if i > 0:
                    temp.append((i - 1, grid[i - 1][j + 1]))
                if i < len(grid) - 1:
                    temp.append((i + 1, grid[i + 1][j + 1]))
                print(j)
                temp.append((i, grid[i][j + 1]))
                for row, num in (temp):
                    if num > grid[i][j]:
                        dfs(row, j + 1, count + 1)
                maxval = max(maxval, count)

        for i in range(len(grid)):
            if maxval == len(grid[0]) - 1:
                return maxval
            dfs(i, 0, 0)
        return maxval
