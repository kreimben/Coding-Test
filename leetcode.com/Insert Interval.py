"""
https://leetcode.com/problems/insert-interval/
Insert Interval
"""
import math
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        target = []
        low, high = math.inf, -math.inf
        for i, (start, end) in enumerate(intervals):
            if start <= newInterval[0] <= end or \
                    start <= newInterval[1] <= end or \
                    newInterval[0] <= start and end <= newInterval[1]:
                target.append(i)
                low = min(low, start, newInterval[0])
                high = max(high, end, newInterval[1])

        if target:
            while target:
                # I have to remove original elements and merge it.
                intervals.pop(target.pop())
            intervals.append([low, high])

        else:
            intervals.append(newInterval)

        return sorted(intervals)


class Solution:
    # Brute force
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval.copy())
        intervals.sort()

        while True:
            # iterate over when not found any changes.
            NOT_CHANGED = True
            remove_target = []
            for i in range(1, len(intervals)):
                if i - 1 in remove_target: continue

                prev, curr = intervals[i - 1], intervals[i]
                if prev[1] >= curr[0] or prev[0] <= curr[0] and prev[1] >= curr[1]:
                    intervals[i - 1][0] = min(prev[0], curr[0])
                    intervals[i - 1][1] = max(prev[1], curr[1])
                    remove_target.append(i)
                    NOT_CHANGED = False

            for index in remove_target:
                intervals.pop(index)

            if NOT_CHANGED: break
        return intervals


class Solution:
    def insert(
            self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res


s = Solution()
assert s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [[1, 5], [6, 9]]
assert s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]) == [[1, 2], [3, 10],
                                                                                               [12, 16]]
