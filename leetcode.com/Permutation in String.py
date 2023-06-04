"""
https://leetcode.com/problems/permutation-in-string/
Permutation in String
"""
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = {}
        for ch in s1:
            if first.get(ch):
                first[ch] += 1
            else:
                first[ch] = 1

        second = defaultdict(int)
        left, right = 0, len(s1) - 1  # don't change gap between left and right.
        block = s2[left:right + 1]
        for ch in block:
            second[ch] += 1

        while right < len(s2):
            if first.items() == second.items():
                return True
            else:
                second[s2[left]] -= 1
                if second[s2[left]] == 0:
                    second.pop(s2[left])
                left += 1
                right += 1
                if right < len(s2):
                    second[s2[right]] += 1
        return False


s = Solution()
assert s.checkInclusion('ab', "eidboaoo") == False
assert s.checkInclusion("ab", "eidbaooo") == True
assert s.checkInclusion("abc", "bbbca") == True
assert s.checkInclusion("adc", "dcda") == True
