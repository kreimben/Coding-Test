"""
https://leetcode.com/problems/longest-cycle-in-a-graph/
Longest Cycle in a Graph
"""
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        maxvalue = -1
        visited = set()

        def dfs(chain: List[int]):
            nonlocal visited, maxvalue
            if chain[-1] == -1:
                return
            visited.add(chain[-1])
            if chain[-1] in chain[:-1]:
                maxvalue = max(maxvalue, len(chain) - chain.index(chain[-1]) - 1)
                return
            dfs(chain + [edges[chain[-1]]])

        for i, target in enumerate(edges):
            if i in visited:
                continue
            dfs([i, target])

        return maxvalue


s = Solution()
assert s.longestCycle([3, 3, 4, 2, 3]) == 3
