"""
https://leetcode.com/problems/meeting-rooms/description/
Meeting Rooms
"""
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0], reverse=True)

        last = None
        while intervals:
            start, end = intervals.pop()
            if not last:
                last = end
                continue
            elif last <= start:
                last = end
            else:
                break
        else:
            return True
        return False
