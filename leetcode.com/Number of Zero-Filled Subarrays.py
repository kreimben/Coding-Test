"""
https://leetcode.com/problems/number-of-zero-filled-subarrays/
Number of Zero-Filled Subarrays
"""
from functools import lru_cache
from typing import List


# class Solution:
# https://leetcode.com/problems/number-of-zero-filled-subarrays/solutions/3321942/python-simple-solution-easy-to-understand/
#     def zeroFilledSubarray(self, nums: List[int]) -> int:
#         total_zero_subarrays = current_zero_subarrays = 0
#
#         for num in nums:
#             if num == 0:
#                 current_zero_subarrays += 1
#                 total_zero_subarrays += current_zero_subarrays
#             else:
#                 current_zero_subarrays = 0
#
#         return total_zero_subarrays

# class Solution:
#     """
#     시간 초과
#     """
#
#     def zeroFilledSubarray(self, nums: [int]) -> int:
#         memo = {0: 0, 1: 1}
#
#         def get_count(n):
#             if n < 0:
#                 return 0
#             for i in range(1, n + 1):
#                 if not memo.get(n, False):
#                     memo[i] = i + memo[i - 1]
#             return memo[n]
#
#         if 0 not in nums:
#             return 0
#
#         res = 0
#
#         left, right = 0, 0
#         while right < len(nums):  # for debug
#             while left < len(nums) and nums[left] != 0:
#                 left += 1
#
#             if left > right:
#                 right = left
#                 continue
#
#             block = nums[left: right + 1]
#
#             if any(block):
#                 right -= 1
#                 count = right - left + 1  # 4 => 4 + 3 + 2 + 1
#                 res += get_count(count)
#                 left = right + 1
#             else:
#                 right += 1
#         else:
#             block = nums[left: right + 1]
#             if left != right and not any(block):
#                 count = right - left
#                 res += get_count(count)
#
#         return res

class Solution:
    """
    faster but 5% beats.
    """

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0

        # get subarray of nums which filled with only 0.
        subarrays = []
        left, right = 0, 0
        while right < len(nums):
            while left < len(nums) and nums[left] != 0:
                left += 1
                continue
            if left > right:
                right = left
                continue

            if nums[right] == 0:
                right += 1
            else:
                subarrays.append(
                    right - left
                )
                left = right
        else:
            if right == len(nums) and nums[right - 1] == 0:
                subarrays.append(
                    right - left
                )

        @lru_cache(maxsize=None)
        def get_count(n: int) -> int:
            if n < 0:
                return 0
            return n + get_count(n - 1)

        for n in subarrays:
            total += get_count(n)

        return total


s = Solution()
assert s.zeroFilledSubarray([0 for _ in range(100_000_000)])
assert s.zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9
assert s.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
