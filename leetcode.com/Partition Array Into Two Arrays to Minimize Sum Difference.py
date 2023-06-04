"""
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
Partition Array Into Two Arrays to Minimize Sum Difference
"""


class Solution:
    def minimumDifference(self, nums: [int]) -> int:
        nums.sort()
        left = []
        right = []
        is_odd = True if (len(nums) // 2) % 2 else False

        if len(nums) == 2:
            return abs(nums[0] - nums[1])
        elif len(nums) == 0:
            return 0

        while nums:
            if len(nums) == 4 and is_odd:
                results = []
                for without in nums:
                    l = left.copy()
                    l.append(without)
                    n = nums.copy()
                    n.remove(without)
                    results.append(abs(sum(l) - sum(n)))
                result = min(results)
                return result
            else:
                first = nums.pop(0)
                last = nums.pop()

                if len(left) <= len(right):
                    left.append(first)
                    left.append(last)
                else:
                    right.append(first)
                    right.append(last)

        return abs(sum(left) - sum(right))


s = Solution()
assert s.minimumDifference([76, 8, 45, 20, 74, 84, 28, 1]) == 2
assert s.minimumDifference([3, 9, 7, 3]) == 2
assert s.minimumDifference([-36, 36]) == -72
assert s.minimumDifference([2, -1, 0, 4, -2, -9]) == 0
