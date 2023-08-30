"""
https://leetcode.com/problems/number-of-islands/
Number of Islands
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        visited = set()
        count = 0
        case = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        )

        def bfs(i, j):
            nonlocal count, case
            q = [(i, j)]
            while q:
                curr = q.pop(0)
                for di, dj in case:
                    x, y = curr[0] + di, curr[1] + dj
                    if (x, y) not in visited and \
                            0 <= x < len(grid) and 0 <= y < len(grid[0]) and \
                            grid[x][y] == '1':
                        visited.add((x, y))
                        q.append((x, y))
            count += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    visited.add((i, j))
                    bfs(i, j)

        return count


from collections import deque


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island = 0
        visit = set()

        def bfs(r: int, c: int):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, up, down

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and
                            c in range(cols) and
                            grid[r][c] == '1' and
                            (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    island += 1
        return island


s = Solution()
assert s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3
assert s.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
