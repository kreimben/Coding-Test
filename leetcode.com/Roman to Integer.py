"""
https://leetcode.com/problems/roman-to-integer/
Roman to Integer
"""

"""
Symbol       Value
I             1
V             5   IV=4
X             10  IX=9
L             50     XL=40
C             100    XC=90
D             500       CD=400
M             1000      CM=900
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        idx = 0
        while True:
            # Wrtie a checking code right after.
            if idx == len(s):
                break
            else:
                tl = s[idx:idx + 2]
                if tl == 'IV':
                    result += 4
                    idx += 2
                    continue
                elif tl == 'IX':
                    result += 9
                    idx += 2
                    continue
                elif tl == 'XL':
                    result += 40
                    idx += 2
                    continue
                elif tl == 'XC':
                    result += 90
                    idx += 2
                    continue
                elif tl == 'CD':
                    result += 400
                    idx += 2
                    continue
                elif tl == 'CM':
                    result += 900
                    idx += 2
                    continue

            ch = s[idx]
            if ch == 'I':
                result += 1
            elif ch == 'V':
                result += 5
            elif ch == 'X':
                result += 10
            elif ch == 'L':
                result += 50
            elif ch == 'C':
                result += 100
            elif ch == 'D':
                result += 500
            elif ch == 'M':
                result += 1000

            idx += 1

        return result


s = Solution()

assert s.romanToInt("III") == 3
assert s.romanToInt("LVIII") == 58
assert s.romanToInt("MCMXCIV") == 1994
