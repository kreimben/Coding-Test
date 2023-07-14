"""
Longest Subarray With Sum
https://www.algoexpert.io/questions/longest-subarray-with-sum
"""

import heapq


def longestSubarrayWithSum(array: [int], targetSum: int):
    left, right = 0, 0
    queue = []

    while right < len(array):
        while left > right:
            right += 1

        block = array[left: right + 1]
        if not block:
            break
        if sum(block) > targetSum:
            left += 1
        elif sum(block) < targetSum:
            right += 1
        else:
            # return [left, right]
            heapq.heappush(queue, (-(right - left), [left, right]))
            right += 1

    return heapq.heappop(queue)[1] if queue else []


assert longestSubarrayWithSum([5], 0) == []
assert longestSubarrayWithSum([0, 0, 0, 0, 39, 0, 0, 0, 0, 0, 28, 10], 39) == [0, 9]
assert longestSubarrayWithSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15) == [0, 4]
