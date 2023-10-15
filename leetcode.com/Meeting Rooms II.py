"""
Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/description/
"""
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        stack = []
        maxval = 0

        for start, end in intervals:
            while stack and stack[-1][1] <= start:
                stack.pop()
            if not stack:
                stack.append((start, end))
            else:
                if stack[-1][1] > start:
                    stack.append((start, end))
            maxval = max(maxval, len(stack))
            stack.sort(key=lambda x: x[1], reverse=True)

        return maxval
