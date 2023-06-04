"""
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
Successful Pairs of Spells and Potions
"""
from bisect import bisect
from typing import List


# class Solution:
#     """
#     Slow and Naïve code
#     """
#     def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
#         potions.sort()
#         res = []
#         N = len(potions)
#
#         for spell in spells:
#             val = ceil(success / spell)
#             while val not in potions and val < max(potions):
#                 val += 1
#             if val in potions:
#                 i = potions.index(val)
#             else:
#                 i = -1
#             if i != -1:
#                 res.append(N - i)
#             else:
#                 res.append(0)
#
#         return res
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array in increasing order.
        potions.sort()
        answer = []

        m = len(potions)
        maxPotion = potions[m - 1]

        for spell in spells:
            # Minimum value of potion whose product with current spell
            # will be at least success or more.
            minPotion = (success + spell - 1) // spell
            # Check if we don't have any potion which can be used.
            if minPotion > maxPotion:
                answer.append(0)
                continue
            # We can use the found potion, and all potion in its right
            # (as the right potions are greater than the found potion).
            index = bisect.bisect_left(potions, minPotion)
            answer.append(m - index)

        return answer
