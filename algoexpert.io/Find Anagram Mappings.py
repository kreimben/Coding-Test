"""
https://leetcode.com/problems/find-anagram-mappings/description/
Find Anagram Mappings
"""
from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [nums2.index(num) for num in nums1]
