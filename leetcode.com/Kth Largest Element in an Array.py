"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
Kth Largest Element in an Array
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = []
        for num in nums:
            heapq.heappush(left, num)
            if len(left) > k:
                heapq.heappop(left)
        return left[0]


s = Solution()
assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
