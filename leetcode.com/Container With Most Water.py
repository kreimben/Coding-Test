"""
https://leetcode.com/problems/container-with-most-water/description/
Container With Most Water
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxval = 0

        while left < right:
            curr = (right - left) * min(height[left], height[right])
            maxval = max(curr, maxval)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxval


s = Solution()
assert s.maxArea([1, 2, 1]) == 2
