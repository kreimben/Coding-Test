"""
https://leetcode.com/problems/merge-k-sorted-lists/
Merge k Sorted Lists
"""
from typing import List, Optional


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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()

        curr = dummy

        while None in lists:
            lists.remove(None)

        while lists:
            min_node = ListNode(float('inf'))
            for node in lists:
                if min_node.val > node.val:
                    min_node = node
            curr.next = min_node
            curr = curr.next
            lists[lists.index(min_node)] = lists[lists.index(min_node)].next
            while None in lists:
                lists.remove(None)

        return dummy.next


# [[1,4,5],[1,3,4],[2,6]]
s = Solution()
assert s.mergeKLists([ListNode(1, ListNode(4, ListNode(5))),
                      ListNode(1, ListNode(3, ListNode(4))),
                      ListNode(2, ListNode(6))])
