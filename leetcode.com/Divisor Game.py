"""
https://leetcode.com/problems/divisor-game/description/
Divisor Game
"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        count = 0
        while n > 1:
            for x in range(1, n):
                if n % x == 0:
                    count += 1
                    n -= x
                    break
            else:
                return False
        return False if count % 2 == 0 else True
