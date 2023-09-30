"""
Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/description/
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0
        prev = intervals[0][1]

        for start, end in intervals[1:]:
            if prev <= start:
                prev = end
            else:
                count += 1
                prev = min(prev, end)

        return count
