"""
https://school.programmers.co.kr/learn/courses/30/lessons/155651
호텔 대실
"""


def get_hour_minute(s: str) -> (int, int):
    s = s.split(':')
    return int(s[0]), int(s[1])


def get_avabile_at(time: [int]) -> (int, int):
    available_at = list(time)
    available_at[1] += 10
    if available_at[1] >= 60:
        available_at[0] += 1
        available_at[1] -= 60
    return available_at


def solution(book_time: [[str]]):
    count = 0

    book_time.sort(key=lambda x: x[0])

    temp = []
    # convert
    for session in book_time:
        temp.append(
            [get_hour_minute(session[0]), get_hour_minute(session[1])]
        )
    book_time = temp
    del temp

    stack: [[int, int]] = []
    for session in book_time:
        start_time = session[0]

        index = 0
        while index < len(stack):
            available_at = get_avabile_at(stack[index][1])
            if available_at[0] <= start_time[0] and available_at[1] <= start_time[1]:
                stack.pop(0)
            else:
                break

        stack.append(session)
        stack.sort(key=lambda x: x[1])
        count = max(count, len(stack))
    return count


assert solution([["09:10", "10:10"], ["10:20", "12:20"]]) == 1
assert solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]) == 3
assert solution([["15:00", "17:00"],
                 ["16:40", "18:20"],
                 ["14:20", "15:20"],
                 ["14:10", "19:20"],
                 ["18:20", "21:20"]]) == 3
