"""
https://leetcode.com/problems/jump-game-ii/description/
Jump Game II
"""
from typing import List


class Solution:
    """
    neetcode.io solution (two pointer)
    O(n)
    """

    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1

        return res

# class Solution:
#     """
#     leetcode solution (editorial)
#     O(n)
#     """
#
#     def jump(self, nums: List[int]) -> int:
#         # The starting range of the first jump is [0, 0]
#         answer, n = 0, len(nums)
#         cur_end, cur_far = 0, 0
#
#         for i in range(n - 1):
#             # Update the farthest reachable index of this jump.
#             cur_far = max(cur_far, i + nums[i])
#
#             # If we finish the starting range of this jump,
#             # Move on to the starting range of the next jump.
#             if i == cur_end:
#                 answer += 1
#                 cur_end = cur_far
#
#         return answer

# class Solution:
#     """
#     Very basic, slow solution. (even can't pass all tests)
#     """
#
#     def jump(self, nums: List[int]) -> int:
#         res = [math.inf]
#
#         def count(i: int, c: int):
#             nonlocal res
#             if i >= len(nums) - 1:
#                 res.append(c)
#                 return
#
#             for amount in range(nums[i], 0, -1):
#                 if c > min(res):
#                     break
#                 count(i + amount, c + 1)
#
#         count(0, 0)
#
#         return min(res)
