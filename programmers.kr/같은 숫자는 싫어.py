"""
https://school.programmers.co.kr/learn/courses/30/lessons/12906
같은 숫자는 싫어
"""


def solution(arr):
    results = []
    for i in range(len(arr)):
        if not i:
            results.append(arr[i])
        elif arr[i - 1] != arr[i]:
            results.append(arr[i])
    return results
