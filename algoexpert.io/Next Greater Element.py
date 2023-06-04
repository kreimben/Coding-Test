"""
https://www.algoexpert.io/questions/next-greater-element
Next Greater Element
"""


def nextGreaterElement(array):
    l = len(array)
    results = [-1] * l
    s = []
    array += array
    for i, num in enumerate(array):
        while s:
            if s and num > s[-1][1]:
                pi, pnum = s.pop()
                results[pi % l] = num
            else:
                break
        s.append((i % l, num))
    return results


assert nextGreaterElement([2, 5, -3, -4, 6, 7, 2]) == [5, 6, 6, 6, 7, -1, 5]
