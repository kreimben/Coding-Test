"""
https://school.programmers.co.kr/learn/courses/30/lessons/42626
더 맵게
"""


def solution(scoville: [int], K: int):
    total_count = 0
    while len(scoville) > 1:
        scoville.sort()

        if K > scoville[0]:
            first = scoville.pop(0)
            second = scoville[0]
            scoville[0] = first + second * 2
            total_count += 1
        else:
            return total_count
    if scoville[0] < K:
        return -1


assert solution([1, 2, 3, 9, 10, 12], 7) == 2
