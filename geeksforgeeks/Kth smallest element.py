"""
Kth smallest element
https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1
"""

import heapq


class Solution:
    def kthSmallest(self, arr: [int], l: int, r: int, k: int):
        heapq.heapify(arr)
        val = None
        index = 0
        while index < k:
            val = heapq.heappop(arr)
            index += 1
        return val
