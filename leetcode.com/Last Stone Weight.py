"""
https://leetcode.com/problems/last-stone-weight/
Last Stone Weight
"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            s = []
            for val in stones:
                heapq.heappush(s, val)
                if len(s) > 2:
                    heapq.heappop(s)

            x, y = s[0], s[1]
            if res := y - x:
                # y - x > 0
                stones.append(res)
            stones.remove(x)
            stones.remove(y)

        return stones[0] if stones else 0


s = Solution()
assert s.lastStoneWeight([2, 2]) == 0
assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
