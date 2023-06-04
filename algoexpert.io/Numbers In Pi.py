"""
https://www.algoexpert.io/questions/numbers-in-pi
Numbers In Pi
"""


# O(length of pi * length of numbers)
def numbersInPi(pi, numbers):
    results = []

    def combine(subtracted, level):
        if len(subtracted) == 0:
            results.append(level - 1)
        # Before I use above numbers, I could find the numbers which only starts with.
        available = list(filter(lambda x: x == subtracted[:len(x)], numbers))
        for number in available:  # 3141, 31
            combine(subtracted[len(number):], level + 1)

    combine(pi, 0)

    return min(results)


assert numbersInPi('3141592', ['3141', '5', '31', '2', '4159', '9', '42']) == 2
