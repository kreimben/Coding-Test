"""
https://leetcode.com/problems/word-break/
Word Break
"""
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:

        @lru_cache(maxsize=None)
        def dfs(string: str):
            if string == '':
                return True

            for word in words:
                N = len(word)
                if len(string) < N:
                    continue
                elif string[:N] == word:
                    res = dfs(string[N:])
                    if res: return True  # res

        return dfs(s)
