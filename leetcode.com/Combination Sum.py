"""
https://leetcode.com/problems/combination-sum/
Combination Sum
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        temp = []
        res = set()

        def backtracking(next: int):
            nonlocal temp, res
            if sum(temp) > target:
                return
            elif sum(temp) == target:
                res.add(tuple(sorted(temp)))
                return

            for i in range(next, len(candidates)):
                temp.append(candidates[i])
                backtracking(i)
                temp.pop()

        backtracking(0)

        return list(res)


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#
#         def dfs(indicies, target):
#             nonlocal res
#             if target == 0:
#                 res.append([candidates[index] for index in indicies])
#                 return
#             elif target < 0:
#                 return
#
#             for i in range(indicies[-1], len(candidates)):
#                 dfs(indicies + [i], target - candidates[i])
#
#         for i, num in enumerate(candidates):
#             dfs([i], target - num)
#
#         return res


s = Solution()
assert s.combinationSum(candidates=[2, 3, 5], target=8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
assert s.combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
