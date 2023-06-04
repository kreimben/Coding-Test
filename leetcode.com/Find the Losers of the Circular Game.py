"""
https://leetcode.com/problems/find-the-losers-of-the-circular-game/
Find the Losers of the Circular Game
"""
from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = [False] * n
        who = 0
        count = 1

        while not visited[who]:
            visited[who] = True
            who = (who + count * k) % n
            count += 1

        res = []
        for i, val in enumerate(visited):
            if val is False:
                res.append(i + 1)

        return res
