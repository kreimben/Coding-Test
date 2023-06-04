"""
https://leetcode.com/problems/word-break/
Word Break
"""
from typing import List


# class Solution:
#     """
#     neetcode.io
#     """
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#
#         dp = [False] * (len(s) + 1)
#         dp[len(s)] = True
#
#         for i in range(len(s) - 1, -1, -1):
#             for w in wordDict:
#                 if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
#                     dp[i] = dp[i + len(w)]
#                 if dp[i]:
#                     break
#
#         return dp[0]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def count(i: int):
            nonlocal res, s
            if i == len(s):
                return True
            elif i > len(s):
                return False
            else:
                res = []
                for w in wordDict:
                    if s[i:i + len(w)] == w and not len(list(filter(lambda x: x is True, res))):
                        res.append(count(i + len(w)))
                return any(res)

        res = []
        for word in wordDict:
            if s[:len(word)] == word and not len(list(filter(lambda x: x is True, res))):
                res.append(count(len(word)))

        return any(res)


s = Solution()
assert s.wordBreak(
    s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    wordDict=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]) == True
assert s.wordBreak(s="leetcode", wordDict=["leet", "code"]) == True
assert s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]) == True
assert s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]) == False
