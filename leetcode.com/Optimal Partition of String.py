"""
https://leetcode.com/problems/optimal-partition-of-string/
Optimal Partition of String
"""


# class Solution:
#     """
#     My code at 2023-04-04
#     """
#
#     def partitionString(self, s: str) -> int:
#         count = 0
#
#         now = defaultdict(int)
#
#         def clean():
#             nonlocal now
#             r = []
#             for k, v in now.items():
#                 if v == 0:
#                     r.append(k)
#             while r:
#                 now.pop(r.pop())
#
#         left, right = 0, 0
#         while right < len(s):
#             executed = False
#             while left > right:
#                 now[s[left]] -= 1
#                 left += 1
#             if executed:
#                 clean()
#
#             if now[s[right]] > 0:
#                 # there are already char.
#                 count += 1
#                 while left != right:
#                     # move left until right.
#                     now[s[left]] -= 1
#                     left += 1
#                 clean()
#                 continue
#
#             now[s[right]] += 1
#
#             right += 1
#
#         return count + 1

class Solution:
    """
    Clever way to solve problem.
    """

    def partitionString(self, s: str) -> int:
        res = 0
        substring = ""
        for ch in s:
            if ch not in substring:
                substring += ch
            else:
                res += 1
                substring = ch
        return res + 1


s = Solution()
assert s.partitionString("ababcbacadefegdehijhklij") == 5
