"""
https://leetcode.com/problems/ransom-note/description/
Ransom Note
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        r = Counter(ransomNote)
        m = Counter(magazine)
        for k, v in r.items():
            mv = m[k]
            if v > mv:
                return False
        return True
