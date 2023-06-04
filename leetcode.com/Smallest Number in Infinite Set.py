"""
https://leetcode.com/problems/smallest-number-in-infinite-set/description/
Smallest Number in Infinite Set
"""
from collections import defaultdict


class SmallestInfiniteSet:

    def __init__(self):
        self.s = defaultdict(bool)
        self.latest = 1

    def popSmallest(self) -> int:
        # tide self.latest
        while self.s[self.latest] is True:
            self.latest += 1
        self.s[self.latest] = True
        self.latest += 1
        return self.latest - 1

    def addBack(self, num: int) -> None:
        self.s[num] = False
        if self.latest >= num:
            self.latest = num

        # Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
