"""
https://school.programmers.co.kr/learn/courses/30/lessons/42748
K번째수
"""


def solution(array, commands):
    results = []
    for command in commands:
        part = array[command[0] - 1: command[1]]
        part.sort()
        results.append(part[(command[2] - 1)])
    return results
