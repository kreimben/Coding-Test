"""
https://school.programmers.co.kr/learn/courses/30/lessons/76501
음양 더하기
"""


def solution(absolutes, signs):
    results = 0
    for index in range(len(absolutes)):
        if not signs[index]:
            results -= absolutes[index]
        else:
            results += absolutes[index]
    return results
