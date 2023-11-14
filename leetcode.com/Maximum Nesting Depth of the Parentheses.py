"""
Maximum Nesting Depth of the Parentheses
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxval = 0
        for ch in s:
            maxval = max(maxval, len(stack))
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                stack.pop()
        return maxval
