"""
https://school.programmers.co.kr/learn/courses/30/lessons/154539
뒤에 있는 큰 수 찾기
"""


def solution(numbers):
    stack = []
    results = [-1 for _ in numbers]

    for i, num in enumerate(numbers):
        while stack:
            topindex, topvalue = stack[-1]
            if topvalue < num:
                stack.pop()
                results[topindex] = num
            else:
                break

        stack.append((i, num))

    return results


assert solution([2, 3, 3, 5]) == [3, 5, 5, -1]
assert solution([9, 1, 5, 3, 6, 2]) == [-1, 5, 6, 6, -1, -1]
