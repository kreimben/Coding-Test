"""
https://www.algoexpert.io/questions/remove-islands
Remove Islands
"""


def removeIslands(matrix):
    # To judge which is island or not,
    # I should store every 1 coordination.
    islands = []
    visited = []
    case = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if (i, j) in visited or matrix[i][j] == 0:
                continue
            temp = []
            queue = []  # ready for bfs
            queue.append((i, j))
            temp.append((i, j))
            while queue:
                ci, cj = queue.pop()
                for ai, aj in case:
                    vi, vj = ci + ai, cj + aj
                    # Finally, We only consider with vi and vj.
                    is_valid = 0 <= vi < len(matrix) and \
                               0 <= vj < len(matrix[0])

                    if is_valid and matrix[vi][vj] == 1 and (vi, vj) not in visited:
                        queue.append((vi, vj))
                        visited.append((vi, vj))
                        temp.append((vi, vj))
            islands.append(temp)

    # After end of counting every land,
    need_to_remove = []
    for island in islands:
        remove = True
        for x, y in island:
            if not (0 < x < len(matrix) - 1 and 0 < y < len(matrix[0]) - 1):
                remove = False
                break

        if remove:
            need_to_remove.append(island)

    for island in need_to_remove:
        for x, y in island:
            matrix[x][y] = 0

    return matrix


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]
expected = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

assert removeIslands(matrix) == expected
