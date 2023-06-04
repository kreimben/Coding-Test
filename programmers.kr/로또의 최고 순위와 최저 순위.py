"""
https://school.programmers.co.kr/learn/courses/30/lessons/77484
로또의 최고 순위와 최저 순위
"""


def solution(lottos, win_nums):
    # Synchronize numbers.
    win_chart = [False for _ in range(45)]
    for num in win_nums:
        win_chart[num - 1] = True

    # Pick what is correct.
    count = 0
    zero = 0
    for num in lottos:
        if num == 0:
            zero += 1
        elif win_chart[num - 1]:
            count += 1

    high = 7 - (count + zero) if count + zero >= 2 else 6
    low = 7 - count if count >= 2 else 6

    return [high, low]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
assert solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) == [3, 5]
assert solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]) == [1, 6]
assert solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) == [1, 1]
