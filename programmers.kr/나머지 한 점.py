"""
https://school.programmers.co.kr/learn/courses/18/lessons/1878?language=python3
나머지 한 점
"""


def solution(v):
    width, height = {}, {}
    for x, y in v:
        width[x] = 1 + width.get(x, 0)
        height[y] = 1 + height.get(y, 0)

    res = []

    for key, value in width.items():
        if value != 2:
            res.append(key)

    # del key, value # just for debbing

    for key, value in height.items():
        if value != 2:
            res.append(key)

    return res
