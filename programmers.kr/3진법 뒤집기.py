"""
https://school.programmers.co.kr/learn/courses/30/lessons/68935
3진법 뒤집기
"""


def solution(n):
    tri = int2base(n, base=3)
    result = ''

    for i in range(len(tri) - 1, -1, -1):
        result += tri[i]

    return three_to_digit(result)


def three_to_digit(s):
    ans = 0
    for c in map(int, s):
        ans = 3 * ans + c
    return ans


import string

digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[x % base])
        x = x // base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


print(solution(45))
assert solution(45) == 7
assert solution(125) == 229
