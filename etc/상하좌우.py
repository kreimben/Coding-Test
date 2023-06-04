"""
이코테 p.110 예제4-1
"""


def solve(n: int = 0, commands: str = ''):
    # Uncomment if real programming OJ.
    # n = int(input())
    # commands = input()
    icon = [1, 1]

    for command in commands.split(' '):
        # print(f'command: {command}')
        icon = move(command, icon, n)

    print(f'icon: {icon}')


def move(command: str, me: [int], limit: int) -> [int]:
    pivot = 0
    pre = 0

    if command == 'L':
        pivot = 1
        pre = me[pivot] - 1

    elif command == 'R':
        pivot = 1
        pre = me[pivot] + 1

    elif command == 'U':
        pivot = 0
        pre = me[pivot] - 1

    elif command == 'D':
        pivot = 0
        pre = me[pivot] + 1

    if pre > 0 and pre <= limit:
        me[pivot] = pre

    return me


solve(5, 'R R R U D D')
