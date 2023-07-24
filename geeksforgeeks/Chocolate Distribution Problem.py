"""
Chocolate Distribution Problem
https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1
"""


class Solution:
    def findMinDiff(self, chocos: [int], N: int, M: int):
        # [3, 4, 1, 9, 56, 7, 9, 12]
        # [1, 3, 4, 7, 9, 9, 12, 56]
        chocos.sort()
        index = 0
        res = []
        while index < len(chocos) - M + 1:
            diff = chocos[index + M - 1] - chocos[index]
            res.append(diff)
            index += 1
        return min(res)
