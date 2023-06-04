"""
https://school.programmers.co.kr/learn/courses/30/lessons/12941
최솟값 만들기
"""


def solution(a: [int], b: [int]):
    # O(n^2)
    # 한 배열의 최댓값과 나머지 배열의 최솟값을 곱하면 되지 않을까...
    a.sort()
    b.sort(reverse=True)
    result = 0

    for _ in range(len(a)):
        result += a.pop(0) * b.pop(0)

    return result


assert solution([1, 4, 2], [5, 4, 4]) == 29
assert solution([1, 2], [3, 4]) == 10
