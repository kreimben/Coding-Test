"""
https://leetcode.com/problems/palindromic-substrings/description/
Palindromic Substrings
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd case
            left, right = i, i
            while -1 < left and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # even case
            left, right = i, i + 1
            while -1 < left and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count
