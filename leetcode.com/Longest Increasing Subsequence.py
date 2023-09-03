"""
https://leetcode.com/problems/longest-increasing-subsequence/
Longest Increasing Subsequence
"""
import heapq


class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = [1] * len(nums)

        def find(i: int) -> int:
            nonlocal dp
            queue = []
            for index in range(i - 1, -1, -1):
                if nums[index] < nums[i]:
                    queue.append((-dp[index], index))

            if not queue:
                return -1
            else:
                heapq.heapify(queue)
                return heapq.heappop(queue)[1]

        for i, num in enumerate(nums):
            if i == 0:
                continue
            elif (tar := find(i)) != -1:
                dp[i] = dp[tar] + 1

        return max(dp)


class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class Solution:
    # Time Limit Exceeded
    def lengthOfLIS(self, nums: [int]) -> int:
        stack = []
        res = 0

        def backtracking(index: int):
            nonlocal stack, res
            if len(stack) > res: res = len(stack)

            if not stack:
                stack.append(nums[index])
                backtracking(index)
                stack.pop()

            else:
                for i in range(index + 1, len(nums)):
                    if stack[-1] < nums[i]:
                        stack.append(nums[i])
                        backtracking(i)
                        stack.pop()

        for i in range(len(nums)):
            backtracking(i)
        return res


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
