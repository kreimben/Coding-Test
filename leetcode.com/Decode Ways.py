"""
https://leetcode.com/problems/decode-ways/
Decode Ways
"""


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         res = 0
#
#         # valid number should be from 1 to 26
#         def calculate(array):
#             nonlocal res
#             if array[-1][1] == len(s) - 1:
#                 for num, _ in array:
#                     if not (len(str(int(num))) == len(num) and 1 <= int(num) <= 26):
#                         break
#                 else:
#                     res += 1
#                 return
#             i = array[-1][1] + 1
#             if i < len(s):
#                 calculate(array + [[s[i], i]])
#             if i + 1 < len(s):
#                 calculate(array + [[s[i: i + 2], i + 1]])
#
#         calculate([[s[0], 0]])
#         calculate([[s[0:2], 1]])
#
#         return res

class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                    s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)


s = Solution()
assert s.numDecodings("226") == 3
assert s.numDecodings('12') == 2
