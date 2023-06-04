"""
https://leetcode.com/problems/daily-temperatures/
Daily Temperatures
"""


class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        stack = []
        results = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                order, value = stack.pop()
                results[order] = i - order

            stack.append((i, v))

        return results


s = Solution()
assert s.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert s.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
