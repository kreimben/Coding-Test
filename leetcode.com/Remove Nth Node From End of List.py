"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Remove Nth Node From End of List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} ({self.next})'

    def __repr__(self):
        return f'{self.val} ({self.next})'


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        # And straight forward until right is null
        while right:
            left = left.next
            right = right.next

        # And traverse until find left
        left.next = left.next.next
        return dummy.next


s = Solution()
assert s.removeNthFromEnd(ListNode(1, ListNode(2)), 2).val == ListNode(2).val
assert s.removeNthFromEnd(ListNode(1), 1) == None
assert s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2) == \
       ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
