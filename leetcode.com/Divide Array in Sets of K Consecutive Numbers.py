"""
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
Divide Array in Sets of K Consecutive Numbers
"""
from typing import List


class Solution:
    """
    not solved
    """

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) / k != len(nums) // k:
            return False
        nums.sort()
        N = len(nums) // k
        s = [[] * N]
        index = 0
        prev = None
        for num in nums:
            if num == prev and prev:
                index += 1
                s.append([])
            if index > N:
                return False
            s[index].append(num)
            prev = num
        return True


s = Solution()
assert s.isPossibleDivide(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3) == True
