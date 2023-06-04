"""
https://leetcode.com/problems/unique-paths/
Unique Paths
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(1 if j == n - 1 or i == m - 1 else 0)
            count.append(row)

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                first = count[i + 1][j]
                second = count[i][j + 1]
                count[i][j] += count[i + 1][j] + count[i][j + 1]

        return count[0][0]


s = Solution()
assert s.uniquePaths(3, 2) == 3
assert s.uniquePaths(3, 7) == 28
