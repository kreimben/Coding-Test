"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
Kids With the Greatest Number of Candies
"""
from typing import List


# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         N = len(candies)
#         pre = [0] * N
#         post = [0] * N
#         res = [False] * N
#
#         # calculate pre
#         for i, candy in enumerate(candies):
#             if i != 0:
#                 pre[i] = max(candies[:i])
#             if i != len(candies) - 1:
#                 post[i] = max(candies[i + 1:])
#
#         for i, candy in enumerate(candies):
#             if pre[i] <= candy + extraCandies and post[i] <= candy + extraCandies:
#                 res[i] = True
#             else:
#                 res[i] = False
#
#         return res

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n, m = len(candies), max(candies)
        return [candy + extraCandies >= m for candy in candies]
