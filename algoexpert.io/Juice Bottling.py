"""
Juice Bottling
https://www.algoexpert.io/questions/juice-bottling
"""


def juiceBottling(prices):
    N = len(prices)  # needed units of goods.

    res = []  # index of goods.
    maxval = 0
    temp = []

    def get_sum():
        nonlocal temp
        return sum(
            [prices[i] for i in temp]
        )

    def backtracking():
        nonlocal res, N, maxval, temp
        if sum(temp) == N - 1:
            if (s := get_sum()) > maxval:
                maxval = s
                res = temp[:]
            return
        elif sum(temp) > N - 1:
            return
        for i in range(1, N):
            if temp and temp[-1] > i: continue
            temp.append(i)
            backtracking()
            temp.pop()

    backtracking()
    return res


assert juiceBottling([0, 2, 3]) == [1, 1]
assert juiceBottling([0, 1, 3, 2]) == [1, 2]
