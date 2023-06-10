"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
Reverse Nodes in K-Group
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        while curr:
            c = curr
            val = []
            for _ in range(k):
                if c is None:
                    break
                val.append(c.val)
                c = c.next
            if not c and len(val) < k:
                break
            c = curr
            for _ in range(k):
                c.val = val.pop()
                c = c.next

            # skip for k
            for _ in range(k):
                curr = curr.next

        return head
