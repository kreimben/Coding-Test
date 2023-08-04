"""
Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/description/
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = list(set(nums))
        q = []
        for key in keys:
            heapq.heappush(q, (-nums.count(key), key))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(q)[1])

        return res


class Solution:
    def topKFrequent(self, nums: List[int], times: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        ready = []
        for k, v in d.items():
            ready.append(
                (v, k)
            )

        ready.sort(key=lambda x: x[0])

        res = []
        for _ in range(times):
            res.append(ready.pop()[1])

        return res
