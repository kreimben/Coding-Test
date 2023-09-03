"""
https://leetcode.com/problems/longest-palindromic-substring/
Longest Palindromic Substring
"""
from functools import lru_cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        for i in range(len(s)):
            # Odd case
            left, right = i, i
            while 0 <= left <= right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

            # Even case
            left, right = i, i + 1
            while 0 <= left <= right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

        return longest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        @lru_cache(maxsize=None)
        def calculate(start, end):
            nonlocal longest
            if start < end and end <= len(s):
                block = s[start:end]
                if block == block[::-1] and len(longest) < len(block):
                    longest = block
                    calculate(end, end + 1)
                calculate(start, end + 1)
                calculate(start + 1, end + 1)

        calculate(0, 1)
        return longest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = ['' for _ in range(len(s) + 1)]
        # None b ba bab baba babad (dp table)
        #  ''  b  b bab bab   bab  (longest palindrome)
        for i in range(1, len(dp)):
            def find(left: int, right: int):
                nonlocal s, i
                if dp[i] != '':
                    return
                while left <= right:
                    if (right - left + 1) <= len(dp[i - 1]):
                        break
                    b = s[left: right + 1]
                    if b == b[::-1]:
                        # Don't need to find further.
                        dp[i] = b
                        break
                    find(left + 1, right)
                    find(left, right - 1)
                    break
                if dp[i] == '':
                    dp[i] = dp[i - 1]

            find(0, i - 1)

        return dp[-1]


s = Solution()
assert s.longestPalindrome("babad") == 'bab'
assert s.longestPalindrome("abb") == 'bb'
assert s.longestPalindrome("cbbd") == 'bb'
assert s.longestPalindrome('aacabdkacaa') == 'aca'
assert s.longestPalindrome("a") == "a"
assert s.longestPalindrome('ac') == 'a'
assert s.longestPalindrome("bb") == 'bb'
