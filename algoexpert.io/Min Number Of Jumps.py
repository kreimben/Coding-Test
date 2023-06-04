"""
https://www.algoexpert.io/questions/min-number-of-jumps
Min Number Of Jumps
"""


def minNumberOfJumps(array):
    if len(array) == 1: return 0

    def make_array(end: int, a) -> [(int, int)]:
        return sorted([(i, a[i]) for i in range(end)], key=lambda x: x[1], reverse=True)

    a = make_array(len(array) - 1, array)
    # I always use index 0 value.
    # So iterate them until I got a chance to land to end.
    minimum = []

    def count_possible(end):
        for i, num in a:
            if i + num >= end:
                # I reached out!
                again(2, i)

    def again(level, end):
        a = make_array(end, array)
        if not a:
            return
        if a[0][0] == 0:
            minimum.append(level)
        else:
            # Iterating this process again.
            for i, num in list(filter(lambda x: x[0] + x[1] >= end, a)):
                again(level + 1, i)

    count_possible(len(a) - 1)

    return min(minimum)


assert minNumberOfJumps([3, 12, 2, 1, 2, 3, 15, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]) == 3
assert minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]) == 4
assert minNumberOfJumps([1]) == 0
