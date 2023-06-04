"""
https://school.programmers.co.kr/learn/courses/30/lessons/12901#
2016년
"""


def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    dim = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = a - 1
    day = b - 1

    day_sum = 0
    for i in range(a - 1):
        print(f'month: {i + 1}')
        # print(f'day sum: {day_sum}')
        print(f'dim: {dim[i]}')
        day_sum += dim[i]
    print(f'day of this month: {day}')
    day_sum += day
    print(f'day sum final: {day_sum}')
    print(f'day module: {day_sum % 7}')

    return days[day_sum % 7]
