"""
https://school.programmers.co.kr/learn/courses/30/lessons/12934
정수 제곱근 판별
"""
from math import sqrt


def solution(n):
    r = sqrt(n)

    check = int(r) ** 2

    if n == check:
        return pow(r + 1, 2)
    else:
        return -1


print(solution(120))
