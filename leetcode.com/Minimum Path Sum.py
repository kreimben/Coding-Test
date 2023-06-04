"""
https://leetcode.com/problems/minimum-path-sum/
Minimum Path Sum
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]):
        # can refer up or left.
        """
        Buttom-Up way
        """
        dp = grid.copy()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    # can't refer up. (only left)
                    dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    # can't refer left. (only up)
                    dp[i][j] += dp[i - 1][j]
                else:
                    # just normal case.
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
    # def minPathSum(self, grid: List[List[int]]):
    #     # can move down or right.
    #     """
    #     Top-Down way
    #     """
    #     @lru_cache(maxsize=None)
    #     def count(x: int, y: int):
    #         nonlocal grid
    #         if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
    #             return None
    #         elif (x == len(grid) - 1) and (y == len(grid[0]) - 1):
    #             return grid[x][y]
    #         elif x == len(grid) - 1:
    #             return count(x, y + 1) + grid[x][y]
    #         elif y == len(grid[0]) - 1:
    #             return count(x + 1, y) + grid[x][y]
    #         else:
    #             return min(filter(lambda x: x is not None, [count(x + 1, y), count(x, y + 1)])) + grid[x][y]
    #
    #     first = count(0, 1)
    #     second = count(1, 0)
    #
    #     if first and second:
    #         return min(first, second) + grid[0][0]
    #     elif first:
    #         return first + grid[0][0]
    #     elif second:
    #         return second + grid[0][0]
    #     else:
    #         return grid[0][0]


s = Solution()
assert s.minPathSum([[0]]) == 0
assert s.minPathSum([[9, 1, 4, 8]]) == sum([9, 1, 4, 8])
