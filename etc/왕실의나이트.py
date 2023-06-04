"""
이코테 p.115 실전 문제 2
"""


def solve(position: str = 'a1'):
    square = 8  # Constant
    # position = input()
    possibility = 0

    # Up 2
    # Check for up space.
    if int(position[1]) - 2 > 0:
        # Check for left-right space.
        if char_convert(to=position[0]) - 2 > 0:
            possibility += 1
        if char_convert(to=position[0]) + 2 < square + 1:
            possibility += 1

    # Down 2
    if int(position[1]) + 2 < square + 1:
        if char_convert(to=position[0]) - 2 > 0:
            possibility += 1
        if char_convert(to=position[0]) + 2 < square + 1:
            possibility += 1

    # Left 2
    if char_convert(position[0]) - 2 > 0:
        if int(position[1]) - 2 > 0:
            possibility += 1
        if int(position[1]) + 2 < square + 1:
            possibility += 1

    # Right 2
    if char_convert(to=position[0]) + 2 < square + 1:
        if int(position[1]) - 2 > 0:
            possibility += 1
        if int(position[1]) + 2 < square + 1:
            possibility += 1

    return possibility


def char_convert(to: str) -> int:
    # No Capital Letters!
    results = ord(to) - 96
    return results


print(solve('a1'))
print(solve('h8'))
print(solve('d4'))
