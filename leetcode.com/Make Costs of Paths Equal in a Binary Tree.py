"""
https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/
Make Costs of Paths Equal in a Binary Tree
"""


class Solution:
    def minIncrements(self, n, cost):
        res = 0

        def dfs(i):
            nonlocal res
            if i >= len(cost): return 0
            a, b = dfs(2 * i + 1), dfs(2 * i + 2)
            res += abs(a - b)
            return cost[i] + max(a, b)

        dfs(0)
        return res

# class Solution:
#     문제 이해 잘못함.
#     def minIncrements(self, n: int, cost: List[int]) -> int:
#         # n => 2 ** level - 1
#         # first. get the level through n.
#         level = int(math.log2(1 + n))
#         # print(f'{level=}')
#
#         flat = [[] * level]
#         curr = 0  # current index in flat.
#
#         for i, num in enumerate(cost):
#             flat[curr].append(num)
#             if len(flat[curr]) >= 2 ** curr:
#                 curr += 1
#                 flat.append([])
#
#         flat.pop()
#
#         # print(f'{flat=}')
#
#         res = []
#
#         for i in range(1, len(flat)):
#             stage = flat[i]
#             while stage:
#                 # pop two things
#                 first = stage.pop()
#                 second = stage.pop()
#                 res.append(abs(first - second))
#
#         return sum(res)
