"""
https://www.algoexpert.io/questions/move-element-to-end
Move Element To End
"""


def moveElementToEnd(array: [int], to_move: int):
    left, right = 0, len(array) - 1

    while left < right:
        if array[right] == to_move:
            right -= 1
            swap_right = False
        else:
            swap_right = True

        if array[left] != to_move:
            left += 1
            swap_left = False
        else:
            swap_left = True

        if swap_left and swap_right:
            array[left], array[right] = array[right], array[left]

    return array


assert moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2) == [4, 1, 3, 2, 2, 2, 2, 2]
