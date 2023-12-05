def solution(edges):
    n = len(edges)

    visited = [False] * (n + 1)

    start_node = 0
    count_donut = 0
    count_bar = 0
    count_eight = 0

    for i in range(n):
        if visited[i]:
            continue

        path = [start_node]
        visited[start_node] = True
        while True:
            if visited[i]:
                break

            next_node = edges[i][0]
            visited[next_node] = True
            path.append(next_node)
            i = next_node

        if len(path) == 2:
            count_bar += 1
        elif len(path) == n:
            count_donut += 1
        elif len(path) == 2 * n + 1:
            count_eight += 1

        start_node = path[-1]

    return [start_node, count_donut, count_bar, count_eight]


s = solution([[2, 3], [4, 3], [1, 1], [2, 1]])
assert s == [2, 1, 1, 0]
