"""
https://leetcode.com/problems/jump-game/description/
Jump Game
"""


class Solution:
    def canJump(self, nums: [int]) -> bool:
        maxjump = nums[0]
        for i, num in enumerate(nums):
            if i > maxjump:
                return False
            maxjump = max(maxjump, i + num)
        return True
