"""
https://leetcode.com/problems/single-number/
Single Number
"""


class Solution:
    def singleNumber(self, nums: [int]) -> int:
        d = {}
        while nums:
            num = nums.pop()
            if d.get(num, None) is not None:
                d.pop(num)
            else:
                d[num] = 1

        result = d.keys()
        return list(result)[0]


s = Solution()
assert s.singleNumber([4, 1, 2, 1, 2]) == 4
