"""
https://school.programmers.co.kr/learn/courses/30/lessons/68644
두 개 뽑아서 더하기
"""


def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result.append(numbers[i] + numbers[j])

    result = list(dict.fromkeys(result))
    result.sort()
    return result


print(solution([2, 1, 3, 4, 1]))
# assert solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7]
# assert solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12]
