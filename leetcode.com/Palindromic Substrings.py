"""
https://leetcode.com/problems/palindromic-substrings/description/
Palindromic Substrings
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd case
            l, r = i, i
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            # even case
            l, r = i, i + 1
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count
