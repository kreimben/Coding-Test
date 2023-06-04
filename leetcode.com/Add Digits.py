"""
https://leetcode.com/problems/add-digits/description/
Add Digits
"""


class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = sum(int(n) for n in str(num))
        return num
