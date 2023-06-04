"""
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
Largest Color Value in a Directed Graph
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        d = defaultdict(list)

        for dep, arr in edges:
            d[dep].append(arr)

        heap = []

        is_circle = False

        def dfs(curr, freq):
            nonlocal d, heap, is_circle
            freq[colors[curr]] += 1
            v = max(freq.values())
            heapq.heappush(heap, (-v, v))
            for n in d[curr]:
                if curr != n:
                    dfs(n, freq.copy())
                else:
                    # it's circling!
                    is_circle = True
                    break

        freq = defaultdict(int)
        for i in range(len(colors)):
            dfs(i, freq.copy())

        if is_circle:
            return -1

        prev = None
        while heap:
            most, _ = heapq.heappop(heap)
            if prev and prev < most:
                return -prev
            prev = most
        return 1


s = Solution()
assert s.largestPathValue("rrrde", [[4, 2], [3, 4], [0, 3], [1, 0], [2, 1]])
assert s.largestPathValue("bbbhb", [[0, 2], [3, 0], [1, 3], [4, 1]]) == 4
assert s.largestPathValue("eeyyeeyeye", [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [4, 6], [5, 7], [6, 8], [8, 9]]) == 5
assert s.largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3
assert s.largestPathValue("a", [[0, 0]]) == -1
