"""
https://www.algoexpert.io/questions/tandem-bicycle
Tandem Bicycle
"""


def tandemBicycle(red_shirt_speeds: [int], blue_shirt_speeds: [int], fastest: bool):
    red_shirt_speeds.sort()
    if fastest:
        blue_shirt_speeds.sort(reverse=True)
    else:
        blue_shirt_speeds.sort()

    result = 0
    while red_shirt_speeds:
        r = red_shirt_speeds.pop(0)
        b = blue_shirt_speeds.pop(0)
        result += max(r, b)

    return result


assert tandemBicycle([1, 2, 1, 9, 12, 3], [3, 3, 4, 6, 1, 2], False) == 30
assert tandemBicycle([9, 8, 2, 2, 3, 5, 6], [3, 4, 4, 1, 1, 8, 9], False) == 35
