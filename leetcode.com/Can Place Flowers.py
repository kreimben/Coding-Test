"""
https://leetcode.com/problems/can-place-flowers/
Can Place Flowers
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                # we can insert to ith element
                # because this problem is just to return true or false of possibility.
                # not minimum or maximum number. So we can insert that.
                f[i] = 1
                n -= 1
        if n > 0:
            return False
        else:
            return True


s = Solution()
assert s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) == False
assert s.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
