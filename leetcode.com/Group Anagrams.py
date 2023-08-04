"""
https://leetcode.com/problems/group-anagrams/
Group Anagrams
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            results[tuple(count)].append(s)
        return results.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[''.join(sorted(s))].append(s)
        return res.values()


s = Solution()

print(
    s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
print(s.groupAnagrams([""]) == [[""]])
print(s.groupAnagrams(["a"]) == [["a"]])
