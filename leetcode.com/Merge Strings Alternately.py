"""
https://leetcode.com/problems/merge-strings-alternately/description/
Merge Strings Alternately
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        word1 = list(word1)
        word2 = list(word2)
        while word1 and word2:
            res += word1.pop(0)
            res += word2.pop(0)

        while word1:
            res += word1.pop(0)

        while word2:
            res += word2.pop(0)

        return res
