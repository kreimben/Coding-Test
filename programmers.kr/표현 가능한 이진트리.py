"""
표현 가능한 이진트리
https://school.programmers.co.kr/learn/courses/30/lessons/150367
"""


def convert(num: int) -> str:
    express = bin(num)[2:]
    n, s = 0, 1
    while s < len(express):
        n += 1
        s += 2 ** n
    return '0' * (s - len(express)) + express


def check(binary: str, dummy: bool = False) -> bool:
    if len(binary) == 1:
        return not dummy or binary == '0'
    root_idx = len(binary) // 2
    root = binary[root_idx]
    if dummy and root == '1':
        return False
    dummy = dummy or root == '0'
    return check(binary[:root_idx], dummy) and check(binary[root_idx + 1:], dummy)


def solution(numbers):
    res = []
    for num in numbers:
        binary = convert(num)
        res.append(
            int(check(binary))
        )

    return res
