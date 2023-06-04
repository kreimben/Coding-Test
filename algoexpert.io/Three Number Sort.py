"""
https://www.algoexpert.io/questions/three-number-sort
Three Number Sort
"""


def threeNumberSort(array, order):
    # To clarify problem,
    # If I remove duplicated elements in array,
    # That will be same as second array (order).
    result = []
    d = {}

    for val in array:
        if d.get(val):
            d[val] += 1
        else:
            d[val] = 1

    for key in order:
        if val := d.get(key):
            result += [key] * val

    return result
