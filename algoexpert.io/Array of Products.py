"""
https://www.algoexpert.io/questions/array-of-products
Array of Products
"""
from collections import defaultdict


def product(arr: [int]):
    result = 1
    for ele in arr:
        result *= ele
    return result


def arrayOfProducts(array: [int]):
    d = defaultdict(int)
    for i in range(len(array)):
        d[i] = product(array[:i]) * product(array[i + 1:])  # without that's product
    return list(d.values())


assert arrayOfProducts([5, 1, 4, 2]) == [8, 40, 10, 20]
