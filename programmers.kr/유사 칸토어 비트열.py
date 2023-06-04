"""
https://school.programmers.co.kr/learn/courses/30/lessons/148652
유사 칸토어 비트열
"""
import math


def get_cantor(n: int, s: str = '1') -> str:
    if n == math.log(len(s), 5):
        return s

    temp = ''
    for ch in s:
        if ch == '1':
            temp += '11011'
        elif ch == '0':
            temp += '00000'

    return get_cantor(n, temp)


def solution(n: int, l: int, r: int):
    result = get_cantor(n)
    result = result[l - 1:r]
    total = 0
    for ch in result:
        if ch == '1':
            total += 1
    return total


assert solution(2, 4, 17) == 8
