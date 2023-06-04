"""
https://leetcode.com/problems/valid-anagram/
Valid Anagram
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for ch in s:
            if not d.get(ch):
                d[ch] = 1
            else:
                d[ch] += 1
        for ch in t:
            if not d.get(ch):
                return False
            else:
                d[ch] -= 1

        for k, v in d.items():
            if v != 0:
                return False

        return True
