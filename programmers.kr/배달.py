"""
https://school.programmers.co.kr/learn/courses/30/lessons/12978
배달
"""

import heapq
from collections import defaultdict


def solution(n, road, k):
    infos = defaultdict(set)
    cost_list = [0] + [n * 10000 for _ in range(n - 1)]

    for start, end, cost in road:
        infos[start].add((end, cost))
        infos[end].add((start, cost))

    heap = [[0, 1]]

    while heap:
        next_one = heapq.heappop(heap)
        if next_one[0] > k:
            continue
        for info in infos[next_one[1]]:
            if cost_list[info[0] - 1] > next_one[0] + info[1]:
                cost_list[info[0] - 1] = next_one[0] + info[1]
                heapq.heappush(heap, [cost_list[info[0] - 1], info[0]])

    return len(list(filter(lambda x: x <= k, cost_list)))


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
