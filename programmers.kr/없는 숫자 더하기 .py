"""
https://school.programmers.co.kr/learn/courses/30/lessons/86051
없는 숫자 더하기
"""


def solution(numbers):
    chart = [False for _ in range(10)]
    result = 0

    for number in numbers:
        chart[number] = True

    for i in range(10):
        if not chart[i]:
            result += i

    return result


print(solution([1,2,3,4,6,7,8,0]))
assert solution([1,2,3,4,6,7,8,0]) == 14
assert solution([5,8,4,0,6,7,9]) == 6