"""
https://leetcode.com/problems/reverse-linked-list-ii/editorial/
Reverse Linked List II
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        prev = None
        curr = head
        next = None

        con = None
        tail = None

        while index <= right:
            if left <= index:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            else:
                con = prev = curr
                curr = curr.next
                tail = curr
            index += 1
        # print(f'{prev=} {curr=} {next=} {con=} {tail=} {head=}')
        if con:
            con.next = prev
        if tail:
            tail.next = curr

        if left == 1:
            return prev
        else:
            return head
