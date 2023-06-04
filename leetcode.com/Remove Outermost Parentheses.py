"""
https://leetcode.com/problems/remove-outermost-parentheses/description/
Remove Outermost Parentheses
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = []
        left, right = 0, 0

        for i, ch in enumerate(s):
            if not stack:
                if ch == '(':
                    stack.append(ch)
                    left = i
            elif len(stack) == 1 and ch == ')':
                res.append(
                    s[left + 1: i]
                )
                stack.pop()
            else:
                if ch == ')':
                    stack.pop()
                    right = i
                else:
                    stack.append(ch)

        return ''.join(res)
