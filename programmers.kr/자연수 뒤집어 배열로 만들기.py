"""
https://school.programmers.co.kr/learn/courses/30/lessons/12932
자연수 뒤집어 배열로 만들기
"""


def solution(n):
    n = str(n)
    r = [c for c in n]
    results = []
    for index in range(len(r)):
        i = len(n) - 1 - index
        results.append(int(r[i]))
    return results


print(solution(12345))
print(solution(54321))
print(solution(482374956827))
print(solution(249687239857))
print(solution(2395879234867))
print(solution(29387102948))
print(solution(2))
