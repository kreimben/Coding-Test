"""
https://school.programmers.co.kr/learn/courses/30/lessons/12920
선입 선출 스케줄링
"""
import heapq


def solution(n, cores):
    """
    1 2 3
    4 2 3
    5 6 3
    """
    N = len(cores)
    heap = []  # (end, core index)
    last_used = None  # last used core index.
    curr = 0  # current time
    rest = [True for _ in range(N)]
    while n > 0:
        while heap and heap[0][0] <= curr:
            _, l = heapq.heappop(heap)
            rest[l] = True

        while n > 0 and \
                len(rest) != len(list(filter(lambda x: x is False, rest))):
            if not any(rest) and heap:
                # if there are no any rest cores.
                end, core_index = heapq.pop(heap)
                last_used = core_index
            else:
                # if there is any rest cores.
                last_used = rest.index(True)  # the very first True index.
            heapq.heappush(heap, (curr + cores[last_used], last_used))
            rest[last_used] = False
            n -= 1
        curr += 1
    return last_used + 1


assert solution(6, [1, 2, 3]) == 2
