"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
Maximum Number of Vowels in a Substring of Given Length
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        criteria = ['a', 'e', 'i', 'o', 'u']
        left, right = 0, k
        count = 0

        res = 0

        for i in range(k):
            if s[i] in criteria:
                count += 1
        res = max(res, count)

        while right < len(s):
            if s[right] in criteria:
                count += 1
            if s[left] in criteria:
                count -= 1

            left += 1
            right += 1

            res = max(res, count)

        return res
