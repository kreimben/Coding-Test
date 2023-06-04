"""
https://school.programmers.co.kr/learn/courses/30/lessons/12980
점프와 순간 이동
"""


def solution(n: int):
    battery_used = 0

    target = n

    while True:
        # First, Reduce 2 times length.
        while True:
            if target % 2 == 0:
                target /= 2
            else:
                break

        target -= 1
        battery_used += 1

        if target == 0:
            break

    return battery_used


print(f'{solution(5)=}')  # 2
print(f'{solution(6)=}')  # 3
print(f'{solution(7)=}')  # 4
print(f'{solution(8)=}')  # 1
print(f'{solution(5000)=}')  # 5
