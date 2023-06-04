"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
Find Words That Can Be Formed by Characters
"""
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            for ch in word:
                if word.count(ch) > chars.count(ch):
                    break
            else:
                ans += len(word)
        return ans
