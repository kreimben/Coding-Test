"""
Valid Parenthesis String
https://leetcode.com/problems/valid-parenthesis-string/
"""
from functools import lru_cache


class Solution:
    def checkValidString(self, s: str) -> bool:

        @lru_cache(maxsize=None)
        def dfs(i: int, string: str) -> bool:
            if i >= len(string):
                return not string
            elif i < 0:
                return False
            elif string[i] == '*':
                # convert to (
                if dfs(i, string[:i] + '(' + string[i + 1:]): return True
                # and )
                if dfs(i, string[:i] + ')' + string[i + 1:]): return True
                # and nothing.
                if dfs(i, string[:i] + string[i + 1:]): return True

                return False

            elif string[i] == '(':
                if not dfs(i + 1, string): return False
            elif string[i] == ')':
                # remove most closiest (
                # that is of course i - 1
                # ((()#
                # 01234
                #    i
                if not dfs(i - 1, string[:i - 1] + string[i + 1:]): return False

            return True

        return dfs(0, s)


s = Solution()
assert s.checkValidString(
    "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())") == False
assert s.checkValidString(
    "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()") == True
