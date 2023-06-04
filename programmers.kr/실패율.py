"""
https://school.programmers.co.kr/learn/courses/30/lessons/42889
실패율
"""


def solution(N, stages):
    over_zero = []
    zero = []

    for index in range(1, N + 1):
        fail = failure(stages, index)
        if fail:
            over_zero.append([index, fail])
        else:
            zero.append(index)

    over_zero.sort(key=lambda x: x[1], reverse=True)
    temp = []
    for num in over_zero:
        temp.append(num[0])
    over_zero = temp
    zero.sort()

    return over_zero + zero


def failure(nums, now):
    all = 0
    in_stage = 0
    for num in nums:
        if num >= now:
            all += 1
        if num == now:
            in_stage += 1
    return in_stage / all if all else 0


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
