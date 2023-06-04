"""
https://leetcode.com/problems/longest-consecutive-sequence/
Longest Consecutive Sequence
"""


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


s = Solution()
assert s.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7
assert s.longestConsecutive([1, 2, 0, 1]) == 3
assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
