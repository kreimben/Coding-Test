"""
https://www.algoexpert.io/questions/find-three-largest-numbers
Find Three Largest Numbers
"""


def findThreeLargestNumbers(array: [int]):
    array.sort()
    return array[-3:]


findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
