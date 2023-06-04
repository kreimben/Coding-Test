"""
https://leetcode.com/problems/car-fleet/
Car Fleet
"""


class Solution:
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:
        """
        Speed will be a coeffecient of equation.
        Position will be a y value of equation.
        From 0 to target, That is range of graph.
        """
        array = list(zip(position, speed))
        array.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for p, s in array:
            stack.append((target - p) / s)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


s = Solution()
assert s.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
assert s.carFleet(10, [0, 4, 2], [2, 1, 3]) == 1
assert s.carFleet(10, [6, 8], [3, 2]) == 2
assert s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
