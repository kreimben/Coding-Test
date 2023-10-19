"""
Hand of Straights
https://leetcode.com/problems/hand-of-straights/
"""
import heapq
from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        rest = Counter(hand)
        q = list(rest.keys())
        heapq.heapify(q)

        while q:
            first = q[0]
            for i in range(first, first + groupSize):
                if i not in rest:
                    return False
                rest[i] -= 1
                if rest[i] == 0:
                    if i != q[0]:
                        return False
                    heapq.heappop(q)

        return True
