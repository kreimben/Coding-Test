"""
https://leetcode.com/problems/maximum-length-of-pair-chain/
Maximum Length of Pair Chain
"""
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # [[1, 2], [4, 5], [7, 8]]
        s = []
        for start, end in pairs:
            if s:
                for room in s:
                    if room[-1][1] < start:
                        room.append((start, end))
                        break
                else:
                    s.append([(start, end)])
            else:
                s.append([(start, end)])
        maxval = 0
        for v in s:
            maxval = max(maxval, len(v))
        return maxval


s = Solution()
assert s.findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2
assert s.findLongestChain([[1, 2], [7, 8], [4, 5]]) == 3
