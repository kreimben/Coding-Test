"""
https://leetcode.com/problems/reverse-linked-list/
Reverse Linked List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next = curr.next  # back up next element for next loop.
            curr.next = prev  # reverse current elements.
            prev = curr  # set current node as prev. i will go to next node.
            curr = next  # go to next node!
        return prev
