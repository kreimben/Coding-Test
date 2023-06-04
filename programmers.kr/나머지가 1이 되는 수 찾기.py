"""
https://school.programmers.co.kr/learn/courses/30/lessons/87389
나머지가 1이 되는 수 찾기
"""


def solution(n):
    for i in range(1, n, 1):
        if n % i == 1:
            return i

print(solution(10))
assert solution(10) == 3
assert solution(12) == 11