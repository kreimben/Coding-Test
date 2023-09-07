"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Longest Substring Without Repeating Characters
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = defaultdict(int)
        maxval = 0

        start = 0
        end = 0
        while end < len(s):
            if curr[s[end]] != 0:
                curr[s[start]] -= 1
                start += 1
            else:
                curr[s[end]] += 1
                maxval = max(maxval, end - start + 1)
                end += 1

        return maxval


s = Solution()
# assert s.lengthOfLongestSubstring("dvdf") == 3
assert s.lengthOfLongestSubstring("pwwkew") == 3
assert s.lengthOfLongestSubstring('aab') == 2
assert s.lengthOfLongestSubstring(' ') == 1
assert s.lengthOfLongestSubstring('   ') == 1
assert s.lengthOfLongestSubstring('au') == 2
