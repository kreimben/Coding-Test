"""
Multiply Strings
https://leetcode.com/problems/multiply-strings/description/
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]

        res = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                res += 10 ** (i + j) * int(num1[i]) * int(num2[j])

        return str(res)
