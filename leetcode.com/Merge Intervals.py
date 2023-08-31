"""
Merge Intervals
https://leetcode.com/problems/merge-intervals/
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        curr = []

        for start, end in intervals:
            if not curr:
                curr = [start, end]
            else:
                if start <= curr[0] <= curr[1] <= end or \
                        curr[0] <= start <= end <= curr[1] or \
                        curr[0] <= start <= curr[1] or \
                        curr[0] <= end <= curr[1]:
                    curr[0] = min(curr[0], start)
                    curr[1] = max(curr[1], end)
                else:
                    res.append(curr.copy())
                    curr = [start, end]
        else:
            if curr:
                res.append(curr.copy())

        return res


s = Solution()
assert s.merge([[0, 0], [1, 2], [5, 5], [2, 4], [3, 3], [5, 6], [5, 6], [4, 6], [0, 0], [1, 2], [0, 2], [4, 5]]) == \
       [0, 6]
