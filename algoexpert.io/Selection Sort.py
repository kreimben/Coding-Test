"""
https://www.algoexpert.io/questions/selection-sort
Selection Sort
"""


def selectionSort(array):
    for i in range(len(array) - 1):
        lowest = min(array[i + 1:])
        if lowest < array[i]:
            li = array.index(lowest, i)
            array[i], array[li] = array[li], array[i]
    return array


assert selectionSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
