"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Longest Substring Without Repeating Characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        d = {}
        maximum = float('-inf')

        while right < len(s) + 1:
            target = right - 1
            if d.get(s[target]):
                # left should be added 1.
                maximum = max(maximum, right - left - 1)
                left += 1
                right += 1

            else:
                # It's valid trial and right should be added 1.
                right += 1
                d[s[target]] = True

        if maximum == float('-inf') or len(d.values()) != 0:
            temp = [value for value in d.values()]
            maximum = max(maximum, sum(temp))

        return maximum


s = Solution()
# assert s.lengthOfLongestSubstring("dvdf") == 3
assert s.lengthOfLongestSubstring("pwwkew") == 3
assert s.lengthOfLongestSubstring('aab') == 2
assert s.lengthOfLongestSubstring(' ') == 1
assert s.lengthOfLongestSubstring('   ') == 1
assert s.lengthOfLongestSubstring('au') == 2
