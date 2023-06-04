"""
https://www.algoexpert.io/questions/nth-fibonacci
Nth Fibonacci
"""


def getNthFib(n: int):
    n -= 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    result = getNthFib(n) + getNthFib(n - 1)

    return result


assert getNthFib(2) == 1
assert getNthFib(3) == 1
assert getNthFib(4) == 2
assert getNthFib(5) == 3
assert getNthFib(6) == 5
