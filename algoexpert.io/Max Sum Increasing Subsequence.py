"""
https://www.algoexpert.io/questions/max-sum-increasing-subsequence
Max Sum Increasing Subsequence
"""


def is_increasing(array) -> bool:
    # Should be strictly increasing!!!
    a = array.copy()
    last = a.pop(0)
    for val in a:
        if last >= val:
            return False
        last = val
    return True


def maxSumIncreasingSubsequence(array):
    if not array:
        return []

    sums = [[array[0], [array[0]]]]

    for i in range(1, len(array)):
        # We should find minimum point.
        small = -1
        for index in range(i + 1):
            if small != -1 and array[small] < array[index] < array[i]:
                small = index
            elif array[index] < array[i]:
                small = index
        if small == -1 or not is_increasing(sums[small][1] + [array[i]]):
            sums.append(
                [
                    array[i],
                    [array[i]]
                ]
            )
        else:
            sums.append(
                [
                    sums[small][0] + array[i],
                    sums[small][1] + [array[i]]
                ]
            )

        if sums[i][0] < array[i]:
            sums[i] = [array[i], [array[i]]]

    return sorted(sums, key=lambda x: x[0], reverse=True)[0]


assert maxSumIncreasingSubsequence([8, 12, 2, 3, 15, 5, 7]) == [35, [8, 12, 15]]
assert maxSumIncreasingSubsequence([-1, 1]) == [1, [1]]
assert maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]) == [110, [10, 20, 30, 50]]
