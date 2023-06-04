"""
https://school.programmers.co.kr/learn/courses/30/lessons/148653
마법의 엘리베이터
"""


def solution(storey: int):
    count = 0
    order = 0

    while True:
        s = str(storey)
        if order > len(s) - 1:
            break

        int_c = int(s[len(s) - 1 - order])

        if int_c > 5:
            storey += 10 ** order
            count += 1
        elif int_c == 0:
            order += 1
        else:
            storey -= 10 ** order
            count += 1

    return count


assert solution(155) == 11
assert solution(154) == 10
assert solution(95) == 6
assert solution(16) == 6
assert solution(2554) == 16
assert solution(6999) == 5  # +1 1번, +1000 3번, -10000 1번
