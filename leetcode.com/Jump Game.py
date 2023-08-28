"""
https://leetcode.com/problems/jump-game/description/
Jump Game
"""
from functools import lru_cache


class Solution:
    def canJump(self, nums: [int]) -> bool:
        if len(nums) == 1: return True

        @lru_cache(maxsize=None)
        def dfs(i: int) -> bool:
            if i >= len(nums) - 1: return True
            for index in range(1, nums[i] + 1):
                res = dfs(i + index)
                if res: return True  # res

        for i in range(1, nums[0] + 1):
            res = dfs(i)
            if res: return True  # res
        return False


class Solution:
    def canJump(self, nums: [int]) -> bool:
        maxjump = nums[0]
        for i, num in enumerate(nums):
            if i > maxjump:
                return False
            maxjump = max(maxjump, i + num)
        return True


s = Solution()
assert s.canJump([0]) is True
assert s.canJump([2, 3, 1, 1, 4]) is True
