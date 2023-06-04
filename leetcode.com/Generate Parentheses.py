"""
https://leetcode.com/problems/generate-parentheses/
Generate Parentheses
"""
from typing import List


class Solution:
    """
    backtracking (neetcode.io solution)
    """

    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(start, end):
            nonlocal stack, res, n
            if start == end == n:
                res.append(''.join(stack))
                return

            if start < n:
                stack.append('(')
                backtracking(start + 1, end)
                stack.pop()

            if end < start:
                stack.append(')')
                backtracking(start, end + 1)
                stack.pop()

        backtracking(0, 0)

        return res


# class Solution:
#     """
#     brute-force way.
#     """
#
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = set()
#
#         def count(s: str):
#             nonlocal res, n
#             start = s.count('(')
#             end = s.count(')')
#             if start == n and end == n:
#                 res.add(s)
#             elif end <= start <= n:
#                 # continue on algorithm.
#                 count(s + '(')
#                 count(s + ')')
#
#         count('(')
#
#         return list(res)


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#
#         @lru_cache(maxsize=None)
#         def find_char_indices(ch: str, s: str) -> List[int]:
#             res = []
#             for i, c in enumerate(s):
#                 if ch == c:
#                     res.append(i)
#             return res
#
#         @lru_cache(maxsize=None)
#         def make(given: str, count: int):
#             nonlocal n, res
#             if count == n:
#                 res.append(given)
#                 return
#             for i in find_char_indices(')', given):
#                 make(given[:i] + '()' + given[i:], count + 1)
#                 make(given[:i + 1] + '()' + given[i + 1:], count + 1)
#
#         make('()', 1)
#         return sorted(list(set(res)))


s = Solution()
assert s.generateParenthesis(3) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
assert s.generateParenthesis(1) == sorted(["()"])
