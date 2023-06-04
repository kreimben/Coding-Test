"""
https://www.algoexpert.io/questions/insertion-sort
Insertion Sort
"""


def insertionSort(array: [int]):
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return array

    left, right = 1, len(array) - 1  # range of unsorted array should be all of initial array!
    while left <= right:
        for i in range(left):
            if array[left] <= array[i]:
                array[left], array[i] = array[i], array[left]
        left += 1

    return array


assert insertionSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
