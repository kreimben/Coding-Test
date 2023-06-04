"""
https://leetcode.com/problems/find-the-distinct-difference-array/
Find the Distinct Difference Array
"""
from collections import defaultdict
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix = {}
        p = [0] * len(nums)
        suffix = defaultdict()
        s = [0] * len(nums)

        nums = [(i, num) for i, num in enumerate(nums)]

        for i, num in nums:
            prefix[num] = 1 + prefix.get(num, 0)
            p[i] = len(prefix.keys())

        for i, num in reversed(nums):
            s[i] = len(suffix.keys())
            suffix[num] = 1 + suffix.get(num, 0)

        return [pre - suf for pre, suf in list(zip(p, s))]
