"""
https://leetcode.com/problems/linked-list-cycle/description/
Linked List Cycle
"""
from collections import defaultdict
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = defaultdict(int)
        curr = head
        while curr and d[curr] < 2:
            d[curr] += 1
            curr = curr.next
        return d[curr] >= 2


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        LIMIT = 10 ** 4 + 1

        count = 0
        curr = head
        while curr and count < LIMIT:
            count += 1
            curr = curr.next

        return count == LIMIT
