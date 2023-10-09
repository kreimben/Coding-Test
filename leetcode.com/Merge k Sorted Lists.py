"""
https://leetcode.com/problems/merge-k-sorted-lists/
Merge k Sorted Lists
"""
import heapq


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
    def mergeKLists(self, lists):
        def merge(node1, node2):
            dummy = ListNode()
            curr = dummy
            while node1 and node2:
                if node1.val < node2.val:
                    curr.next = node1
                    node1 = node1.next
                else:
                    curr.next = node2
                    node2 = node2.next
                curr = curr.next
            else:
                curr.next = node1 if node1 else node2

            return dummy.next

        while len(lists) > 1:
            for _ in range(len(lists) // 2):
                lists.append(
                    merge(lists[0], lists[1])
                )
                lists.pop(0)
                lists.pop(0)

        return lists


class Solution:
    def mergeKLists(self, lists):
        q = []

        for head in lists:
            curr = head
            while curr:
                q.append(curr.val)
                curr = curr.next

        heapq.heapify(q)

        res = ListNode()  # dummy
        curr = res
        while q:
            child = ListNode(val=heapq.heappop(q))
            curr.next = child
            curr = curr.next

        return res.next


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         dummy = ListNode()
#
#         curr = dummy
#
#         while None in lists:
#             lists.remove(None)
#
#         while lists:
#             min_node = ListNode(float('inf'))
#             for node in lists:
#                 if min_node.val > node.val:
#                     min_node = node
#             curr.next = min_node
#             curr = curr.next
#             lists[lists.index(min_node)] = lists[lists.index(min_node)].next
#             while None in lists:
#                 lists.remove(None)
#
#         return dummy.next


# [[1,4,5],[1,3,4],[2,6]]
s = Solution()
assert s.mergeKLists([ListNode(1, ListNode(4, ListNode(5))),
                      ListNode(1, ListNode(3, ListNode(4))),
                      ListNode(2, ListNode(6))])
