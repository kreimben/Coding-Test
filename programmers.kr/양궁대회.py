"""
https://school.programmers.co.kr/learn/courses/30/lessons/92342
양궁대회
"""


def calc_point(apeach, lion):
    apeach_score = 0
    lion_score = 0
    for i in range(11):
        if apeach[i] == lion[i] == 0:
            continue
        if apeach[i] >= lion[i]:
            apeach_score += 10 - i
        else:
            lion_score += 10 - i
    return lion_score - apeach_score


# 지금쏘는 과녁 idx, 남은 화살 개수, 어피치점수, 내점수
def dfs(idx: int, n: int, apeach: [int], lion: [int]):
    global answer, point
    if n < 0:
        return
    # 점수 계산
    if idx > 10:
        diff = calc_point(apeach, lion)
        if diff <= 0:
            return
        if diff > point:
            point = diff
            answer = [lion[i] for i in range(11)]
            answer[10] += n
        return

    # 상대가 쏜 점수보다 높이 쏴본다
    lion[10 - idx] = apeach[10 - idx] + 1
    # 다음 점수. 재귀 호출 (스택)을 이용한 dfs풀이. 남은 화살의 갯수에서 지금 라이언이 쏜 갯수만큼 적다.
    dfs(idx + 1, n - lion[10 - idx], apeach, lion)
    lion[10 - idx] = 0
    dfs(idx + 1, n, apeach, lion)


def solution(n, info):
    global answer, point
    answer = [-1]
    point = 0
    dfs(idx=0, n=n, apeach=info, lion=[0 for _ in range(11)])
    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
