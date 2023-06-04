"""
https://leetcode.com/problems/number-of-closed-islands/
Number of Closed Islands
"""
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # should not touch edge side of grid.
        visited = set()
        case = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        count = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 1 or (i, j) in visited:
                    continue
                visited.add((i, j))
                q = [(i, j)]
                while q:
                    x, y = q.pop(0)
                    for vi, vj in case:
                        row, col = x + vi, y + vj
                        if (row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1) and \
                                grid[row][col] == 0:
                            # invalidate this trial because current point has touched to the edge of grid.
                            count -= 1
                            break
                        elif 0 < row < len(grid) - 1 and 0 < col < len(grid[0]) - 1 and \
                                (row, col) not in visited and grid[row][col] == 0:
                            visited.add((row, col))
                            q.append((row, col))
                count += 1
        return count


s = Solution()
assert s.closedIsland([
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
]) == 5
assert s.closedIsland([[0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]) == 1
