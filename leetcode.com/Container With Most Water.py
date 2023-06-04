"""
https://leetcode.com/problems/container-with-most-water/description/
Container With Most Water
"""


class Solution:
    def maxArea(self, height: [int]) -> int:
        max_area = 0

        left, right = 0, len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


s = Solution()
assert s.maxArea([1, 2, 1]) == 2
