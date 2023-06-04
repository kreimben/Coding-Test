# def solution(people, limit):
#     people.sort()
#     case = 0
#     on_board = [False for _ in people]
#     for i in range(len(people) - 1, -1, -1):
#         boat = 0
#         boat_people = 0
#         if on_board[i]:
#             continue
#         for j in range(i, -1, -1):
#             person = people[j]
#             if boat_people >= 2:
#                 break
#             elif boat + person <= limit:
#                 boat += person
#                 boat_people += 1
#                 on_board[j] = True
#
#         case += 1
#
#     return case

from collections import deque


def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    while deq:
        if len(deq) == 1:
            answer += 1
            break
        if deq[0] + deq[-1] <= limit:
            deq.pop()
            deq.popleft()
        else:
            deq.pop()
        answer += 1
    return answer


assert solution([70, 50, 80, 50], 100) == 3
assert solution([70, 80, 50], 100) == 3
# print(solution([70, 80, 50], 100))
assert solution([40, 40, 40], 120) == 2
assert solution([40, 40, 40, 50, 50, 60, 70, 80], 100) == 5
