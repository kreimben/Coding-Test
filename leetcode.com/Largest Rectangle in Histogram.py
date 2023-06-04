"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
Largest Rectangle in Histogram
"""


class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area


s = Solution()
assert s.largestRectangleArea([3, 6, 5, 7, 4, 8, 1, 0]) == 20
assert s.largestRectangleArea([2, 1, 2]) == 3
assert s.largestRectangleArea([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 12
assert s.largestRectangleArea([1]) == 1
assert s.largestRectangleArea([2, 4]) == 4
assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
