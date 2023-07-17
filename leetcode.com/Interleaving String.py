"""
Interleaving String
https://leetcode.com/problems/interleaving-string/description/?source=submission-noac
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        cache = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        def is_valid(i, j):
            nonlocal cache
            if cache[i][j] is not None:
                return cache[i][j]

            k = i + j
            if k == len(s3):
                return True

            if i < len(s1) and s1[i] == s3[k]:
                cache[i][j] = is_valid(i + 1, j)
                if cache[i][j]:
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                cache[i][j] = is_valid(i, j + 1)
                if cache[i][j]:
                    return True

            return False

        return is_valid(0, 0)


s = Solution()
assert s.isInterleave("a", "", "c") == False
