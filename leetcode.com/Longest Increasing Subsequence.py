"""
https://leetcode.com/problems/longest-increasing-subsequence/
Longest Increasing Subsequence
"""


class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = [(1, nums[0]) for _ in range(len(nums))]  # LIS count, starting value

        for i in range(1, len(nums)):
            prev, curr = nums[i - 1], nums[i]
            n = nums[i]
            if prev < curr:
                dp[i] = (dp[i - 1][0] + 1, dp[i - 1][1])
            elif dp[i - 1][1] <= nums[i]:
                dp[i] = dp[i - 1]
            else:  # if prev == curr:
                dp[i] = (1, nums[i])
        return dp[-1][0]


s = Solution()
assert s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
assert s.lengthOfLIS([4, 10, 4, 3, 8, 9]) == 3
assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
