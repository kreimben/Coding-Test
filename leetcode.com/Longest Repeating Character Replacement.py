"""
https://leetcode.com/problems/longest-repeating-character-replacement/description/
Longest Repeating Character Replacement
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        left = 0
        maxval = 0
        for right in range(len(s)):
            d[s[right]] = 1 + d.get(s[right], 0)
            many_key = sorted(d, key=d.get, reverse=True)[0]
            if (right - left + 1) - d[many_key] > k:
                d[s[left]] -= 1
                left += 1
            else:
                maxval = max(maxval, (right - left + 1))
        return maxval


s = Solution()
assert s.characterReplacement("BAAAB", 2) == 5
assert s.characterReplacement("ABBB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
