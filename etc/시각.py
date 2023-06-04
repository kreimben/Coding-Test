"""
이코테 p.113 예제 4-2
"""


def solve(hour: int):
    # hour = int(input())

    counter = 0
    for h in range(hour + 1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h) + str(m) + str(s):
                    counter += 1

    print(f'counter: {counter}')
    return counter


solve(5)
