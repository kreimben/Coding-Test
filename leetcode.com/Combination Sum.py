"""
https://leetcode.com/problems/combination-sum/
Combination Sum
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(indicies, target):
            nonlocal res
            if target == 0:
                res.append([candidates[index] for index in indicies])
                return
            elif target < 0:
                return

            for i in range(indicies[-1], len(candidates)):
                dfs(indicies + [i], target - candidates[i])

        for i, num in enumerate(candidates):
            dfs([i], target - num)

        return res


s = Solution()
assert s.combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
