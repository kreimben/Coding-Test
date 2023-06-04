"""
https://school.programmers.co.kr/learn/courses/30/lessons/60057
문자열 압축
"""


def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        tmp = ''
        idx = 0
        while idx < len(s):
            current = s[idx:idx + i]
            shorted_count = 1

            while current == s[idx + i: idx + i + i]:
                idx += i
                shorted_count += 1

            tmp += ((str(shorted_count) + current) if shorted_count != 1 else current)
            idx += i

        answer = len(tmp) if len(tmp) < answer else answer
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
