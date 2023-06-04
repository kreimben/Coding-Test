"""
https://school.programmers.co.kr/learn/courses/30/lessons/154540
무인도 여행
"""


def solution(maps):
    our_map = []
    for i, row in enumerate(maps):
        for j, ch in enumerate(row):
            if len(our_map) <= i:
                our_map.append([])

            our_map[i].append(ch)

    # BFS
    results = []
    visited = []
    queue = []
    list_for = [(0, 0), (0, 1), (1, 0), (-1, 0), (0, -1)]
    for i, row in enumerate(our_map):
        for j, col in enumerate(row):
            if (i, j) in visited:
                continue

            queue.append((i, j))
            count = 0
            while queue:
                c_i, c_j = queue.pop()
                for v in list_for:
                    v_x = c_i + v[0]
                    v_y = c_j + v[1]
                    if v_x < 0 or v_y < 0 or len(our_map) - 1 < v_x or len(our_map[0]) - 1 < v_y:
                        continue

                    if (v_x, v_y) in visited:
                        continue

                    current = our_map[v_x][v_y]
                    if current != 'X':
                        count += int(current)
                        if (v_x, v_y) not in queue:
                            queue.append((v_x, v_y))
                    if (v_x, v_y) not in visited:
                        visited.append((v_x, v_y))
            if count != 0:
                results.append(count)
    return sorted(results) if results else [-1]


assert solution(["XXX", "XXX", "XXX"]) == [-1]
assert solution(["X591X", "X1X5X", "X231X", "1XXX1"]) == [1, 1, 27]
