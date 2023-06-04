"""
https://www.algoexpert.io/questions/knapsack-problem
Knapsack Problem
"""


def get_knapsack_items(values, items):
    sequence = []
    i = len(values) - 1
    c = len(values[0]) - 1
    while i > 0:
        if values[i][c] == values[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))


def knapsackProblem(items: [[int]], capacity: int):
    values = []  # To make j represents number of capacity.
    for i in range(len(items) + 1):
        values.append([0] * (capacity + 1))

    for i in range(1, len(items) + 1):  # Don't add 1 cuz already added empty values to values.
        v = items[i - 1][0]
        w = items[i - 1][1]
        for j in range(capacity + 1):
            if w <= j:
                values[i][j] = max(values[i - 1][j], values[i - 1][j - w] + v)
            else:
                values[i][j] = values[i - 1][j]  # Just inherit them exactly.

    return [values[-1][-1], get_knapsack_items(values, items)]


assert knapsackProblem([
    [1, 2],
    [4, 3],
    [5, 6],
    [6, 7]
], 10) == [10, [1, 3]]
