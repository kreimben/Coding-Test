"""
https://www.algoexpert.io/questions/spiral-traverse
Spiral Traverse
"""


def spiralTraverse(array: [[int]]):
    result = []
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])
        start_row += 1

        if start_row > end_row:
            break

        for row in range(start_row, end_row + 1):
            result.append(array[row][end_col])
        end_col -= 1

        if start_col > end_col:
            break

        for col in reversed(range(start_col, end_col + 1)):
            result.append(array[end_row][col])
        end_row -= 1

        for row in reversed(range(start_row, end_row + 1)):
            result.append(array[row][start_col])
        start_col += 1

    return result


assert spiralTraverse([
    [1],
    [3],
    [2],
    [5],
    [4],
    [7],
    [6]
]) == [1, 3, 2, 5, 4, 7, 6]
assert spiralTraverse([
    [1, 2, 3],
    [12, 13, 4],
    [11, 14, 5],
    [10, 15, 6],
    [9, 8, 7]
]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
assert spiralTraverse([
    [1]
]) == [1]
assert spiralTraverse([
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
