"""
https://leetcode.com/problems/add-binary/description/
Add Binary
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(
            int(a, 2) + int(b, 2)
        )
