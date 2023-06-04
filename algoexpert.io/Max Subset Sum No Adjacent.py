"""
https://www.algoexpert.io/questions/max-subset-sum-no-adjacent
Max Subset Sum No Adjacent
"""


def maxSubsetSumNoAdjacent(array):
    if not array: return 0
    avail = [0] * len(array)

    for i, num in enumerate(array):
        search_start = i - 2  # cuz we have to explore aleast two indexes before.
        if search_start >= 0:
            ready = max(avail[:search_start + 1]) + num
        else:
            ready = num

        avail[i] = ready

    return max(avail)


assert maxSubsetSumNoAdjacent([10, 5, 20, 25, 15, 5, 5, 15]) == 60
