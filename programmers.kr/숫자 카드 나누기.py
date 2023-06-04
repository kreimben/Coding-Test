"""
https://school.programmers.co.kr/learn/courses/30/lessons/135807
숫자 카드 나누기
"""
import functools
import math


def solution(array_a: [int], array_b: [int]):
    a_gcd = functools.reduce(math.gcd, array_a)
    b_gcd = functools.reduce(math.gcd, array_b)

    a_right = False
    b_right = False

    if b_gcd != 1:
        for a_num in array_a:
            if a_num % b_gcd == 0:
                break
        else:
            a_right = True

    if a_gcd != 1:
        for b_num in array_b:
            if b_num % a_gcd == 0:
                break
        else:
            b_right = True

    if a_right and b_right:
        return max(a_gcd, b_gcd)
    elif a_right:
        return b_gcd
    elif b_right:
        return a_gcd
    else:
        return 0


assert solution([10, 17], [5, 20]) == 0
assert solution([10, 20], [5, 17]) == 10
assert solution([14, 35, 119], [18, 30, 102]) == 7
