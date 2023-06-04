"""
https://school.programmers.co.kr/learn/courses/30/lessons/42587#
프린터
"""


def solution(priorities, location):
    count = 0
    target = location
    queue = priorities

    while queue:
        if max(queue) == queue[0]:
            queue.pop(0)
            count += 1
            if not target:
                return count
            else:
                target -= 1
        else:
            temp = queue.pop(0)
            queue += [temp]
            if target == 0:
                target = len(queue) - 1
            else:
                target -= 1

    return count


print(solution([2, 1, 3, 2], 2) == 1)
print(solution([1, 1, 9, 1, 1, 1], 0) == 5)
