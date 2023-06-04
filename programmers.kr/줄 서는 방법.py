"""
https://school.programmers.co.kr/learn/courses/30/lessons/12936
줄 서는 방법
"""
import itertools
import math


def dfs(n: int, target: int, a: [int], results: [int]):
    if len(results) == target:
        return
    elif len(a) == n:
        results.append(a)
    else:
        for num in range(1, n + 1):
            if num not in a:
                dfs(n, target, a + [num], results)


def solution(n: int, k: int):
    results = []

    dfs(n, k, [], results)

    return results[k - 1]


def test(n: int, k: int):
    case = itertools.permutations(range(1, n + 1), n)
    result = solution(n, k)
    c = list(case)[k - 1]
    print(f'{result=}, case={c}')
    assert result == list(c)


for i in range(20):
    for j in range(1, math.factorial(i)):
        print(f'{i=}, {j=}')
        test(i, j)
