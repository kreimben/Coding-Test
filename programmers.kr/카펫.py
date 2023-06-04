"""
https://school.programmers.co.kr/learn/courses/30/lessons/42842
카펫
"""


def solution(brown, yellow):
    total = brown + yellow

    cases = []

    for n in range(1, total + 1):
        if total % n == 0 and n >= total // n >= 3:
            cases.append([n, total // n])

    for case in cases:
        if ((case[0] - 2) * (case[1] - 2)) == yellow:
            return case

    return 0


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
