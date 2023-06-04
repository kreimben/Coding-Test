"""
https://www.algoexpert.io/questions/minimum-waiting-time
Minimum Waiting Time
"""


def minimumWaitingTime(queries: [int]):
    queries.sort()
    result = 0
    for i in range(len(queries) - 1, -1, -1):
        result += i * queries.pop(0)

    return result


assert minimumWaitingTime([3, 2, 1, 2, 6]) == 17
assert minimumWaitingTime([1, 2, 4, 5, 2, 1]) == 23
