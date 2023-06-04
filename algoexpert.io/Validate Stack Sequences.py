"""
https://leetcode.com/problems/validate-stack-sequences/description/
Validate Stack Sequences
"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        while pushed or popped:
            if pushed:
                if s and s[-1] == popped[0]:
                    popped.pop(0)
                    s.pop()
                else:
                    s.append(pushed.pop(0))
            else:
                # should compare rest elements in stack and popped.
                if s.pop() != popped.pop(0):
                    return False
        return True
