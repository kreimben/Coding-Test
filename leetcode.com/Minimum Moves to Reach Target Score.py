"""
https://leetcode.com/problems/minimum-moves-to-reach-target-score/description/
Minimum Moves to Reach Target Score
"""


class Solution(object):
    def minMoves(self, target, maxDoubles):
        return self.dfs(target, maxDoubles, 0)

    def dfs(self, target, maxDoubles, count):
        if target == 1:
            return count
        if maxDoubles > 0:
            if target % 2 == 0:
                return self.dfs(target // 2, maxDoubles - 1, count + 1)
            else:
                return self.dfs(target - 1, maxDoubles, count + 1)
        else:
            return count + target - 1
