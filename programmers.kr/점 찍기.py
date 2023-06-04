"""
https://school.programmers.co.kr/learn/courses/30/lessons/140107
점 찍기
"""

from math import sqrt, ceil


def solution(k: int, d: int) -> int:
    count = 0

    for i in range(0, d + 1, k):
        # x^2 + y^2 <= d^2을 찾자
        # y^2 <= d^2 - x^2
        max_y = sqrt((d ** 2) - (i ** 2))
        count += ceil(max_y / k) + (1 if (max_y % k) == 0 else 0)

    return count


assert solution(2, 4) == 6
assert solution(1, 5) == 26
