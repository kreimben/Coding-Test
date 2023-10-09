"""
Merge Triplets to Form Target Triplet
https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
"""
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 50% performance record. Not bad.
        curr = [0, 0, 0]

        for one, two, three in triplets:
            if one > target[0] or two > target[1] or three > target[2]:
                continue
            curr[0] = max(curr[0], one)
            curr[1] = max(curr[1], two)
            curr[2] = max(curr[2], three)

        if curr == target:
            return True
        else:
            return False


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Brute-Force and Time Limit Exceeded
        N = len(triplets)
        for i in range(N):
            for j in range(N):
                if i == j: continue
                one, two = triplets[i], triplets[j]
                if one[0] > target[0] or one[1] > target[1] or one[2] > target[2] or \
                        two[0] > target[0] or two[1] > target[1] or two[2] > target[2]:
                    continue
                triplets[j][0] = max(triplets[i][0], triplets[j][0])
                triplets[j][1] = max(triplets[i][1], triplets[j][1])
                triplets[j][2] = max(triplets[i][2], triplets[j][2])

                if target == triplets[j]:
                    return True

        if target == triplets[-1]:
            return True

        return False
