"""
https://school.programmers.co.kr/learn/courses/30/lessons/12985
예상 대진표
"""


def solution(n: int, a: int, b: int):
    people = [False] * n

    for i in range(n):
        if i + 1 == a or i + 1 == b:
            people[i] = True

    count = 0
    while True:
        new_people = [False] * (len(people) // 2)
        is_end_for_loop = False
        for i, person in enumerate(new_people):
            if people[i * 2] is True and people[i * 2 + 1] is True:
                is_end_for_loop = True
                break
            elif people[i * 2]:
                new_people[i] = True
            elif people[i * 2 + 1]:
                new_people[i] = True
        count += 1

        if is_end_for_loop:
            break

        people = new_people

    return count


print(solution(8, 1, 2) == 1)
print(solution(8, 2, 3) == 2)
print(solution(8, 4, 7) == 3)
