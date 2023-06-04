"""
https://leetcode.com/problems/group-anagrams/
Group Anagrams
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        results = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            results[tuple(count)].append(s)
        return results.values()


s = Solution()

print(
    s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
print(s.groupAnagrams([""]) == [[""]])
print(s.groupAnagrams(["a"]) == [["a"]])
