"""
https://www.algoexpert.io/questions/bubble-sort
Bubble Sort
"""


def bubbleSort(array: [int]):
    find_count = 0
    while True:
        find_count = 0
        for i, v in enumerate(array):
            if i != len(array) - 1:  # if i is not last.
                if array[i] > array[i + 1]:
                    find_count += 1
                    array[i], array[i + 1] = array[i + 1], array[i]
        if not find_count:
            break

    return array


assert bubbleSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
