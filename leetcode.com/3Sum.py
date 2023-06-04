"""
https://leetcode.com/problems/3sum/
3Sum
"""


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        results = []

        for i, v in enumerate(nums):
            if i != 0 and nums[i - 1] == nums[i]:
                continue

            target = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp = target + nums[left] + nums[right]
                if temp == 0:
                    results.append([v, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif temp > 0:
                    right -= 1
                elif temp < 0:
                    left += 1

        return results


s = Solution()
assert s.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]) == [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4],
                                                              [-3, 0, 3], [-3, 1, 2], [-2, -1, 3],
                                                              [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
