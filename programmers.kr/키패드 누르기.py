"""
https://school.programmers.co.kr/learn/courses/30/lessons/67256
키패드 누르기
"""


def solution(numbers, hand):
    results = ''
    l = '*'
    r = '#'

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            results += 'L'
            l = f'{number}'
        elif number == 3 or number == 6 or number == 9:
            results += 'R'
            r = f'{number}'
        else:
            l_dis = distance(l, number)
            r_dis = distance(r, number)
            if l_dis > r_dis:
                results += 'R'
                r = f'{number}'
            elif l_dis < r_dis:
                results += 'L'
                l = f'{number}'
            elif l_dis == r_dis:
                if hand == 'left':
                    results += 'L'
                    l = f'{number}'
                elif hand == 'right':
                    results += 'R'
                    r = f'{number}'

    return results


def distance(current, by_far):
    chart = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    loc = []

    for i in range(len(chart)):
        for j in range(len(chart[i])):
            if str(current) == chart[i][j]:
                loc.append([i, j])
            if str(by_far) == chart[i][j]:
                loc.append([i, j])

    x = abs(loc[0][0] - loc[1][0])
    y = abs(loc[0][1] - loc[1][1])

    return x + y
