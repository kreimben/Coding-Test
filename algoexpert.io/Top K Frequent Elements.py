"""
https://leetcode.com/problems/top-k-frequent-elements/
Top K Frequent Elements
"""
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        d = defaultdict(int)
        results = []

        for num in nums:
            d[num] += 1

        return [num for (num, _) in sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]]
