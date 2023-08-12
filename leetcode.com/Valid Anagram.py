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


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_keys = set(list(s))  # a, n, g, r, m
        t_keys = set(list(t))  # n, a, g, r, m

        if s_keys != t_keys:
            return False

        # compare
        for key in s_keys:
            if s.count(key) != t.count(key):
                return False

        return True
