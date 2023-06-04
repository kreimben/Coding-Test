"""
https://school.programmers.co.kr/learn/courses/30/lessons/77884?language=python3
약수의 개수와 덧셈
"""


def solution(left, right):
    result = 0
    for num in range(left, right + 1, 1):
        is_odd = get_devided_count(num) % 2
        if is_odd:
            # Odd Number.
            result -= num
        else:
            # Even Number.
            result += num
    return result


def get_devided_count(num: int) -> int:
    count = 0
    for i in range(1, num + 1, 1):
        if num % i == 0:
            count += 1
    return count


print(solution(13, 17))
assert solution(13, 17) == 43
assert solution(24, 27) == 52