"""
https://school.programmers.co.kr/learn/courses/30/lessons/42890
후보키
"""
from functools import cmp_to_key


def check(relation, rowsize, colsize, subset):
    """
    Check uniqueness.
    """
    for a in range(rowsize - 1):
        for b in range(a + 1, rowsize):
            is_same = True
            for k in range(colsize):
                if (subset & 1 << k) == 0:
                    # k is not included in subset.
                    continue
                if relation[a][k] != relation[b][k]:
                    is_same = False
                    break
            if is_same:
                return False
    return True


def compare(a, b):
    """
    Check minimality.
    """
    x = bin(a).count('1')
    y = bin(b).count('1')
    return x - y


def solution(relation: [[str]]):
    answer = 0
    rowsize = len(relation)
    colsize = len(relation[0])
    candidates = []

    for i in range(1 << colsize):
        if check(relation, rowsize, colsize, i):
            candidates.append(i)

    candidates = sorted(candidates, key=cmp_to_key(compare))

    while len(candidates) != 0:
        n = candidates.pop(0)
        answer += 1
        candidates = [x for x in candidates if (n & x) != n]

    return answer


test_val1 = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"],
             ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"],
             ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
test_val2 = [["100", "ryan"], ["200", "apeach"],
             ["300", "tube"], ["400", "con"]]
test_val3 = [["music", "2"], ["math", "2"],
             ["computer", "3"], ["computer", "4"],
             ["music", "3"], ["music", "2"]]
print(solution(test_val1))
