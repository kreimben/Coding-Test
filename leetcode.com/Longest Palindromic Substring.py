"""
https://leetcode.com/problems/longest-palindromic-substring/
Longest Palindromic Substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = ['' for _ in range(len(s) + 1)]
        # None b ba bab baba babad (dp table)
        #  ''  b  b bab bab   bab  (lognest palindrom)
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
                        # Don't need to find furthur.
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
