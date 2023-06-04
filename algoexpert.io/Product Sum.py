"""
https://www.algoexpert.io/questions/product-sum
Product Sum
"""


def find_factorial(n: int) -> int:
    total = 1
    while n != 0:
        total *= n
        n -= 1
    return total


def calculate(array: [], level: int):
    # This function take care of "purely" integers.
    # If array include the arrays, Call it-self again in loop.
    sum = 0
    for element in array:
        if isinstance(element, int):
            sum += element * find_factorial(level)
        else:
            sum += calculate(element, level + 1)
    return sum


def productSum(array: []):
    return calculate(array, 1)


assert productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12  # 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
assert productSum([[[[[5]]]]]) == 600
