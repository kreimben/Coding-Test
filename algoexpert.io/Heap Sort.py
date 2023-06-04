"""

Heap Sort
"""


def push(array, value):
    array.append(value)
    # check it from start to end.
    child = len(array) - 1
    while (parent := (child - 1) // 2) > -1:
        if array[parent] > array[child]:
            array[parent], array[child] = array[child], array[parent]
        child = parent


def pop(array) -> int:
    result = array.pop(0)
    # Re arrange heap.
    child = len(array) - 1
    while (parent := (child - 1) // 2) > -1:
        if array[parent] > array[child]:
            array[parent], array[child] = array[child], array[parent]
        child -= 1
    return result


def heapSort(array):
    # Just sort with (min) heap.
    q = []
    for val in array:
        push(q, val)

    result = []
    while q:
        result.append(
            pop(q)
        )
    return result


assert heapSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
