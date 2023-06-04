"""
https://school.programmers.co.kr/learn/courses/30/lessons/152996
시소 짝꿍
"""


def solution(weights: [int]):
    """
    관계는
    1:1
    2:1
    2:3
    3:4
    4가지 케이스로만 나뉠 수 있다.
    """
    result = 0
    for i in range(len(weights) - 1):
        for j in range(i + 1, len(weights)):
            first = weights[i]
            second = weights[j]
            if first == second or \
                    first * 2 == second * 3 or first * 3 == second * 2 or \
                    first * 2 == second or first == second * 2 or \
                    first * 3 == second * 4 or first * 4 == second * 3:
                result += 1

    return result


assert solution([100, 180, 360, 100, 270]) == 4
