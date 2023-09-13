"""
https://leetcode.com/problems/reorder-list/
Reorder List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get middle node of list nodes.
        mid, end = head, head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        if end:
            mid = mid.next

        # cut off head after mid
        curr = head
        while curr.next != mid:
            curr = curr.next
        curr.next = None

        def reverse(node: ListNode) -> ListNode | None:
            prev: ListNode | None = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            return prev

        mid = reverse(mid)

        # assemble
        curr = head
        while curr and mid:
            next = curr.next
            midnext = mid.next
            curr.next = mid
            curr.next.next = next

            curr = curr.next.next
            mid = midnext

        return curr
