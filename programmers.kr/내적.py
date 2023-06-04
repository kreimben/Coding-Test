"""
https://school.programmers.co.kr/learn/courses/30/lessons/70128
내적
"""


def solution(a, b):
    result = 0
    for index in range(len(a)):
        result += a[index] * b[index]
    return result
