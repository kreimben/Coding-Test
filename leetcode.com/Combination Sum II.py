"""
https://leetcode.com/problems/combination-sum-ii/
Combination Sum II
"""
from typing import List


# class Solution:
#     """
#     wrong code.
#     """
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()  # [1, 1, 2, 5, 6, 7, 10]
#         res = []  # indicies.
#
#         def count(chain: [int]):
#             nonlocal res, candidates, target
#             c = [candidates[i] for i in chain]
#             # s = sum(c)
#             if sum(c) == target:
#                 c = [candidates[i] for i in chain]
#                 if c not in res:
#                     res.append(c)
#                 return
#             elif sum(c) > target:
#                 return
#             last = chain[-1] + 1
#             if last >= len(candidates):
#                 return
#             count(chain + [last])
#             chain.pop()
#             count(chain + [last])
#
#         count([0])
#
#         return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res


s = Solution()
s.combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27)
assert s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8) == [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6]
]
