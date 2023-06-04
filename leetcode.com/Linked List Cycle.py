"""
https://leetcode.com/problems/linked-list-cycle/description/
Linked List Cycle
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # All I need to do is just check that next is duplicated.
        d = {}
        curr = head
        d[curr] = True
        while curr:
            if d.get(curr.next, False):
                # Duplicated!
                return True
            d[curr.next] = True
            curr = curr.next
        return False
