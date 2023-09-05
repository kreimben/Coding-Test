"""
https://leetcode.com/problems/longest-repeating-character-replacement/description/
Longest Repeating Character Replacement
"""
from collections import defaultdict

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         d = {}
#         left = 0
#         maxval = 0
#         for right in range(len(s)):
#             d[s[right]] = 1 + d.get(s[right], 0)
#             many_key = sorted(d, key=d.get, reverse=True)[0]
#             if (right - left + 1) - d[many_key] > k:
#                 d[s[left]] -= 1
#                 left += 1
#             else:
#                 maxval = max(maxval, (right - left + 1))
#         return maxval
#
#
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         # brute force
#         keys = list(set(list(s)))
#
#         def count(i: int, string: str, left: int) -> int:
#             # just return biggest number in `string`.
#             nonlocal keys
#             if len(s) <= i:
#                 prev = None
#                 maxval = 0
#                 d = defaultdict(int)
#                 string += ' '
#                 for c in string:
#                     d[c] += 1
#                     if prev != c:
#                         maxval = max(maxval, d[prev])
#                         d[prev] = 0
#                     prev = c
#                 return maxval
#
#             if left:
#                 res = 0
#                 # changing following for-loop
#                 for char in keys:
#                     if string[i] == char: continue
#                     res = max(
#                         res,
#                         count(i + 1, string[:i] + char + string[i + 1:], left - 1)
#                     )
#                 # not changing
#                 res = max(res, count(i + 1, string, left))
#                 return res
#             else:
#                 return count(i + 1, string, 0)
#
#         res = count(0, s, k)
#         if k:
#             for char in keys:
#                 if s[0] == char: continue
#                 res = max(res, count(0, char + s[1:], k - 1))
#         return res


from functools import lru_cache

SPECIAL_CHAR = '@'


@lru_cache(maxsize=None)
def get_max_val(s: str) -> int:
    d = defaultdict(int)
    left, right = 0, 0
    maxval = 0
    while right < len(s):
        d[s[right]] += 1
        if s[right] == SPECIAL_CHAR:
            right += 1
            continue
        if len(d.keys()) > 1 and SPECIAL_CHAR not in d.keys() or \
                len(d.keys()) > 2 and SPECIAL_CHAR in d.keys():
            total = 0
            for v in d.values():
                total += v
            maxval = max(maxval, total - d[s[right]])
            d = defaultdict(int)
            left = right
            while s[left] == SPECIAL_CHAR:
                left -= 1
                d[s[left]] += 1
        else:
            right += 1
    maxval = max(maxval, sum(d.values()))
    return maxval


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def count(index: int, string: str, left: int) -> int:
            if left == 0 or index == len(string):
                return get_max_val(string)

            # not changing. just pass.
            res = count(index + 1, string, left)

            # changing with `SPESIAL_CHAR`.
            res = max(
                res,
                count(index + 1, string[:index] + SPECIAL_CHAR + string[index + 1:], left - 1)
            )

            return res

        return count(0, s, k)


s = Solution()
# assert s.characterReplacement("BAAAB", 2) == 5
assert s.characterReplacement("ABBB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
