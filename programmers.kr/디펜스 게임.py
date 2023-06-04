"""
https://school.programmers.co.kr/learn/courses/30/lessons/142085
디펜스 게임
"""


def is_defence(n: int, k: int, e: [int]) -> bool:
    total = 0

    for _ in range(k):
        e.remove(max(e))

    for enemy in e:
        if total + enemy > n:
            return False
        else:
            total += enemy

    return True


def solution(n: int, k: int, enemies: [int]):
    if k >= len(enemies): return len(enemies)

    left, right = 0, len(enemies)

    while left < right:
        target = (left + right) // 2

        if is_defence(n, k, enemies[:target]):
            left = target
        else:
            right = target - 1

    return right


assert solution(7, 3, [4, 2, 4, 5, 3, 3, 1]) == 5
assert solution(2, 4, [3, 3, 3, 3]) == 4
