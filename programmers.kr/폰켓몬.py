"""
https://school.programmers.co.kr/learn/courses/30/lessons/1845
폰켓몬
"""


def solution(nums):
    nums.sort()
    count = 0
    maximum = (len(nums) / 2)

    for index in range(len(nums)):
        if not index:
            count += 1
        elif nums[index - 1] == nums[index]:
            continue
        else:
            count += 1
    return count if count <= maximum else maximum
