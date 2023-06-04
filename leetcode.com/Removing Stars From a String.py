"""
https://leetcode.com/problems/removing-stars-from-a-string/description/
Removing Stars From a String
"""


# class Solution:
#     """
#     Too slow.
#     """
#     def removeStars(self, s: str) -> str:
#         while '*' in s:
#             i = s.index('*')
#             left = i
#             while -1 < left:
#                 if s[left] != '*':
#                     break
#                 else:
#                     left -= 1
#             if s[left] == '*':
#                 # I can't!
#                 break
#             else:
#                 s = s[:left] + s[left + 1:]
#                 s = s[:i - 1] + s[i:]
#         return s

class Solution:
    def removeStars(self, s: str) -> str:
        S = []
        for c in s:
            if c == '*':
                S.pop()
                continue
            S.append(c)
        return ''.join(S)
