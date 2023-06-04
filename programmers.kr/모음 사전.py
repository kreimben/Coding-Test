"""
https://school.programmers.co.kr/learn/courses/30/lessons/84512
모음 사전
"""


def recursive(n: int, w: str, results: [int]):
    case = ['', 'A', 'E', 'I', 'O', 'U']

    if n == 0:
        results.append(w)
        return

    for i in range(6):
        recursive(n - 1, w + case[i], results)


def solution(word: str) -> int:
    results = []

    recursive(5, '', results)

    results = sorted(list(set(results)))

    result = results.index(word)
    return result


assert solution("AAAAE") == 6
assert solution("EIO") == 1189
