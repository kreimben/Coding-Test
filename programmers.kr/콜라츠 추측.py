"""
https://school.programmers.co.kr/learn/courses/30/lessons/12943
콜라츠 추측
"""


def solution(num: int):
    count = 0

    for index in range(500):
        if num == 1:
            return count
        elif num % 2 == 0:
            num /= 2
            count += 1
        else:
            num *= 3
            num += 1
            count += 1

    return -1


assert solution(6) == 8
assert solution(16) == 4
assert solution(626331) == -1
