"""
https://www.algoexpert.io/questions/river-sizes
River Sizes
"""


def riverSizes(matrix: [[int]]):
    # Use BFS
    case = [
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1)
    ]
    visited = []
    queue = []
    results = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) in visited or matrix[i][j] == 0:
                continue

            count = 1

            queue.append((i, j))
            visited.append((i, j))

            while queue:
                q_i, q_j = queue.pop()
                for add_x, add_y in case:
                    curr_x = q_i + add_x
                    curr_y = q_j + add_y

                    if 0 <= curr_x < len(matrix) and \
                            0 <= curr_y < len(matrix[0]):
                        if (curr_x, curr_y) in visited:
                            # We can skip that.
                            continue
                        elif matrix[curr_x][curr_y] == 1:
                            count += 1
                            queue.append((curr_x, curr_y))
                            visited.append((curr_x, curr_y))

            # After and of each case, Calculate
            if count != 0:
                results.append(count)

    return sorted(results)


assert riverSizes([
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]) == [1, 2, 2, 2, 5]
