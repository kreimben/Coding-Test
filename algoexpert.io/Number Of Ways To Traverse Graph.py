"""
https://www.algoexpert.io/questions/number-of-ways-to-traverse-graph
Number Of Ways To Traverse Graph
"""


def numberOfWaysToTraverseGraph(width, height):
    maps = []

    for _ in range(width):
        maps.append([0] * height)

    for i in range(width):
        for j in range(height):
            if i == 0 or j == 0:
                maps[i][j] = 1

    for i in range(1, width):
        for j in range(1, height):
            maps[i][j] += maps[i - 1][j] + maps[i][j - 1]

    return maps[width - 1][height - 1]


assert numberOfWaysToTraverseGraph(4, 3) == 10
