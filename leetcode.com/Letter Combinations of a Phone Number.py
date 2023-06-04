"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Letter Combinations of a Phone Number
"""
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        # 어차피 어떤 숫자가 오든지 경우의 수는 3^n이다.
        # 예를 들어 23이 온다면 3^2의 경우의 수를 가진다.
        # for문으로 돌리면 시간 제한을 통과할리가 없으니
        # 다른 방법으로 알아보자.
        if len(digits) == 0:
            return []

        case = []

        while digits:
            ch = digits[:1]
            if '2' == ch:
                case.append(['a', 'b', 'c'])
            elif '3' == ch:
                case.append(['d', 'e', 'f'])
            elif '4' == ch:
                case.append(['g', 'h', 'i'])
            elif '5' == ch:
                case.append(['j', 'k', 'l'])
            elif '6' == ch:
                case.append(['m', 'n', 'o'])
            elif '7' == ch:
                case.append(['p', 'q', 'r', 's'])
            elif '8' == ch:
                case.append(['t', 'u', 'v'])
            elif '9' == ch:
                case.append(['w', 'x', 'y', 'z'])

            digits = digits[1:]

        results = list(product(*case))

        return [''.join(x) for x in results]


s = Solution()

assert s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert s.letterCombinations("") == []
assert s.letterCombinations('2') == ["a", "b", "c"]
assert s.letterCombinations('22') == ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
