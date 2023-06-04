"""
https://leetcode.com/problems/triangle/
Triangle
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0 for _ in range(len(triangle[-1]) + 1)]

        for nums in triangle[::-1]:
            for i, num in enumerate(nums):
                dp[i] = min(dp[i], dp[i + 1]) + num

        return dp[0]


# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         dp = [[None] * len(triangle[-1]) for _ in range(len(triangle))]
#
#         def count(curr_row, curr_col):
#             if curr_row + 1 < len(triangle) and dp[curr_row][curr_col] is None:
#                 f = count(curr_row + 1, curr_col)
#             else:
#                 f = 0
#
#             if curr_row + 1 < len(triangle) and dp[curr_row][curr_col + 1] is None:
#                 s = count(curr_row + 1, curr_col + 1)
#             else:
#                 s = 0
#
#             if dp[curr_row][curr_col] is None:
#                 dp[curr_row][curr_col] = min(f, s) + triangle[curr_row][curr_col]
#
#             return dp[curr_row][curr_col]
#
#         return count(0, 0)


s = Solution()
assert s.minimumTotal([[2], [3, 4], [6, 5, 9], [4, 4, 8, 0]]) == 14
assert s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
