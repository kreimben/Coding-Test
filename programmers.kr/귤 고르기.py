"""
https://school.programmers.co.kr/learn/courses/30/lessons/138476
귤 고르기
"""

from collections import Counter


def solution(k: int, tangerine: [int]) -> int:
    tangs = Counter(tangerine)

    results = 0
    total = 0
    for _, count in tangs.most_common():
        if k > total:
            total += count
            results += 1

    return results


assert solution(6, [1, 3, 2, 5, 4, 5, 2, 3]) == 3
assert solution(4, [1, 3, 2, 5, 4, 5, 2, 3]) == 2
assert solution(2, [1, 1, 1, 1, 2, 2, 2, 3]) == 1
