"""
https://school.programmers.co.kr/learn/courses/30/lessons/12947
하샤드 수
"""


def solution(x):
    n = str(x)
    s = 0
    for c in n:
        s += int(c)

    if x % int(s):
        return False
    else:
        return True


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
