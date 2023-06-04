"""
https://leetcode.com/problems/minimum-window-substring/
Minimum Window Substring
"""
from collections import Counter
from unittest import TestCase


class Solution:
    """
    풀었던 문제 다시 풀기
    """

    def minWindow(self, s: str, t: str) -> str:
        for ch in t:
            if ch not in s or t.count(ch) > s.count(ch):
                return ''

        left, right = 0, 0
        need = Counter(t)
        res = s

        def clean():
            nonlocal need
            removal = []
            for k, v in need.items():
                if v == 0:
                    removal.append(k)
            while removal:
                need.pop(removal.pop())

        def fit() -> bool:
            nonlocal need
            for k, v in need.items():
                if v > 0:
                    return False
            return True

        while right < len(s):
            while left < len(s) and s[left] not in t:
                left += 1
            else:
                if left > right:
                    right = left
                if left >= len(s):
                    break

            block = s[left: right + 1]  # just for debugging.
            for k, v in need.items():
                if v < 0 and s[left] == k:
                    need[s[left]] += 1
                    left += 1
                    clean()
                    break
            else:
                if s[right] in t:
                    need[s[right]] -= 1
                    clean()
                if fit():
                    if len(res) > len(s[left: right + 1]):
                        res = s[left: right + 1]
                    if s[left] in t:
                        need[s[left]] += 1
                    left += 1

                right += 1

        return res


class Case(TestCase):
    s = Solution()

    def test1(self):
        actual = self.s.minWindow("ADOBECODEBANC", "ABC")
        expected = 'BANC'
        self.assertEqual(expected, actual)

    def test2(self):
        actual = self.s.minWindow('ab', 'b')
        expected = 'b'
        self.assertEqual(expected, actual)

    def test3(self):
        actual = self.s.minWindow('a', 'aa')
        exected = ''
        self.assertEqual(exected, actual)

    def test4(self):
        actual = self.s.minWindow('a', 'a')
        expected = 'a'
        self.assertEqual(expected, actual)

    def test5(self):
        actual = self.s.minWindow('a', 'b')
        expected = ''
        self.assertEqual(expected, actual)

    def test6(self):
        actual = self.s.minWindow('bba', 'ba')
        expected = 'ba'
        self.assertEqual(expected, actual)

    def test7(self):
        actual = self.s.minWindow('ab', 'a')
        expected = 'a'
        self.assertEqual(expected, actual)
