"""
https://leetcode.com/problems/longest-consecutive-sequence/
Longest Consecutive Sequence
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)

        longest = 0
        for num in nums:
            if num - 1 not in num_set:
                # It is starting point!
                length = 0
                while (num + length) in num_set:
                    length += 1
                if length > longest:
                    longest = length
        return longest


from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)  # 0 or 1

        nums = sorted(list(set(nums)))

        chart = defaultdict(int)
        for num in nums:
            chart[num] += 1

        combo = 1
        maxval = 0
        key = 0

        while key <= len(nums) - 1:
            if chart[nums[key]] and chart[nums[key] + 1]:  # much faster than using string as key.
                combo += 1
            else:
                maxval = max(maxval, combo)
                combo = 1
            key += 1

        return max(maxval, combo)


s = Solution()
assert s.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7
assert s.longestConsecutive([1, 2, 0, 1]) == 3
assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
