"""
https://leetcode.com/problems/search-a-2d-matrix/
Search a 2D Matrix
"""


class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        row_left, row_right = 0, len(matrix) - 1
        col_left, col_right = 0, len(matrix[0]) - 1

        while row_left < row_right:
            if matrix[row_left][col_right] < target:
                row_left += 1

            if matrix[row_right][col_left] > target:
                row_right -= 1

        while col_left < col_right:  # If it's possible to reach this while loop, The row is perfect to search in col.
            mat = matrix[row_left]

            if mat[col_left] == target or mat[col_right] == target: return True

            if mat[col_left] < target:
                col_left += 1
            if mat[col_right] > target:
                col_right -= 1

        if matrix[row_left][col_left] == target:
            return True
        else:
            return False


s = Solution()
assert s.searchMatrix([[1, 1]], 2) == False
assert s.searchMatrix([[1]], 1) == True
assert s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13) == False
assert s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3) == True
