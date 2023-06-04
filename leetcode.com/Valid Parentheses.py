"""
https://leetcode.com/problems/valid-parentheses/
Valid Parentheses
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if stack:
                if ch == ')':
                    top = stack.pop()
                    if top != '(':
                        return False
                elif ch == ']':
                    top = stack.pop()
                    if top != '[':
                        return False
                elif ch == '}':
                    top = stack.pop()
                    if top != '{':
                        return False
                else:
                    stack.append(ch)
            elif ch != ')' and ch != ']' and ch != '}':
                stack.append(ch)
            else:
                return False

        return False if stack else True


s = Solution()
assert s.isValid("{[]}") == True
assert s.isValid("]") == False
assert s.isValid('[') == False
assert s.isValid("()") == True
assert s.isValid("()[]{}") == True
assert s.isValid("(]") == False
