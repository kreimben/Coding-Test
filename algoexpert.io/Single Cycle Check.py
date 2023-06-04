"""

Single Cycle Check
"""


def hasSingleCycle(array):
    visited = []  # store visited index.

    index = 0
    while len(array) + 1 != len(visited):
        visited.append(index)

        jump = array[index % len(array)]
        next = (index + jump) % len(array)
        index = next

    if len(list(set(visited))) != len(array) or visited[0] != visited[-1]:
        return False
    else:
        return True


assert hasSingleCycle([1, -1, 1, -1]) == False
assert hasSingleCycle([1, 1, 1, 1, 2]) == False
assert hasSingleCycle([2, 3, 1, -4, -4, 2]) == True
