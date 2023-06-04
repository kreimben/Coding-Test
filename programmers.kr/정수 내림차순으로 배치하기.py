"""
https://school.programmers.co.kr/learn/courses/30/lessons/12933
정수 내림차순으로 배치하기
"""


def solution(n):
    n = str(n)
    n = [c for c in n]
    n.sort(reverse=True)
    results = ''
    for c in n:
        results += str(c)
    return int(results)


print(solution(118372))
