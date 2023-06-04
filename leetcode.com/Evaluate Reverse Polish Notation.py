"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
Evaluate Reverse Polish Notation
"""


class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) + int(second))
            elif token == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) - int(second))
            elif token == '*':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) * int(second))
            elif token == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(int(first) / int(second)))

            else:
                stack.append(token)

        return int(stack.pop())


s = Solution()
assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
