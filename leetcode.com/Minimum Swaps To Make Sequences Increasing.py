"""
Minimum Swaps To Make Sequences Increasing
https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
"""
import math
from typing import List


class Solution:
    # not solved yet.
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        minval = math.inf

        # @lru_cache(maxsize=None)
        def dfs(i: int) -> int | float:
            # `i` is target index that should be swapped.
            if i >= len(nums1): return math.inf
            # first, swap it
            if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                nums1[i], nums2[i] = nums2[i], nums1[i]
                res = []

                for index in range(i, len(nums1)):
                    prev1, curr1 = nums1[index - 1], nums1[index]
                    prev2, curr2 = nums2[index - 1], nums2[index]

                    if prev1 >= curr1 or prev2 >= curr2:
                        res.append(dfs(index - 1) + 1)
                        res.append(dfs(index) + 1)
                        res.append(dfs(index + 1) + 1)

                # after business logic, recover them.
                nums1[i], nums2[i] = nums2[i], nums1[i]
                # print(f'{i=} {min(res, default=1)}')
                return min(res, default=1)
            else:
                return math.inf

        for i in range(1, len(nums1)):
            prev1, curr1 = nums1[i - 1], nums1[i]
            prev2, curr2 = nums2[i - 1], nums2[i]

            if prev1 >= curr1 or prev2 >= curr2:
                minval = min(minval, dfs(i - 1))
                minval = min(minval, dfs(i))
                minval = min(minval, dfs(i + 1))
                # print(f'{i=} {minval=}')
                break

        return minval if minval != math.inf else 0
