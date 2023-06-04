"""
https://school.programmers.co.kr/learn/courses/30/lessons/12977
소수만들기
"""


def solution(nums):
    nums.sort()
    case = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i >= j or j >= k or i >= k:
                    continue

                num = nums[i] + nums[j] + nums[k]
                if is_prime(num):
                    case.append(num)

    return len(case)


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
