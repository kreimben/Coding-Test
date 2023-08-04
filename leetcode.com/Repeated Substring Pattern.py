"""
Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for mid in range(len(s) // 2, 0, -1):
            if len(s) % mid == 0:
                q = len(s) // mid
                if s[:mid] * q == s:
                    return True
        else:
            return False
