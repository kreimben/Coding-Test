"""
https://leetcode.com/problems/max-area-of-island/
Max Area of Island
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0

        case = [
            (0, 0),
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        visited = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue

                area = 1
                q = [(i, j)]
                visited.append((i, j))

                while q:
                    ii, jj = q.pop()
                    for ai, aj in case:
                        ci, cj = ii + ai, jj + aj

                        if 0 <= ci < len(grid) and 0 <= cj < len(grid[0]) and \
                                (ci, cj) not in visited and \
                                grid[ci][cj] == 1:
                            q.append((ci, cj))
                            visited.append((ci, cj))
                            area += 1
                maxarea = max(maxarea, area)
        return maxarea


s = Solution()
actual = s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
expected = 6
assert actual == expected
