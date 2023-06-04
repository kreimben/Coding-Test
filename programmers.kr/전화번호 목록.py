"""
https://school.programmers.co.kr/learn/courses/30/lessons/42577
전화번호 목록
"""


def solution(p):
    p.sort()
    for i in range(len(p) - 1):
        first = p[i]
        second = (p[i + 1])[:len(p[i])]
        if first == second:
            return False

    return True


assert solution(["119", "97674223", "1195524421"]) == False
assert solution(["123", "456", "789"]) == True
assert solution(["12", "123", "1235", "567", "88"]) == False
