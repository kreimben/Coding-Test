"""
https://school.programmers.co.kr/learn/courses/30/lessons/118668?language=python3
코딩 테스트 공부
"""
from queue import PriorityQueue


def solution(alp: int, cop: int, problems: [[int]]):
    total_time = 0
    max_alp_req = 0
    max_cop_req = 0
    INF = int(1e9)

    for i, p in enumerate(problems):
        # find max things
        if max_alp_req < p[0]:
            max_alp_req = p[0]
        if max_cop_req < p[1]:
            max_cop_req = p[1]

    left_alp = max_alp_req - alp
    left_cop = max_cop_req - cop

    """
    10, 11 (left_alp, left_cop)로 가기 위해
    2, 1 증가 2 소모
    3, 1 증가 2 소모
    4, 0 증가 2 소모
    0, 4 증가 2 소모
    되는 방법들이 있다고 하자. 이들 중에서 최단 거리(최소 시간)을 구하면 된다.
    """

    q = PriorityQueue()

    # 최소시간이 우선순위로 와야한다.
    for p in problems:
        q.put((p[4], p[2], p[3]))

    while q:
        if not q.empty():
            _, this_alp_rwd, this_cop_rwd = q.get()
        else:
            break  # quit main loop

        if left_alp - this_alp_rwd == 0:
            break

        if left_cop - this_cop_rwd == 0:
            break


# assert solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]) == 15
solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])  # == 13
