"""
https://leetcode.com/problems/palindrome-linked-list/description/
Palindrome Linked List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'{self.val} ({self.next})'


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    almost closed with neetcode.io's solution.
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            # when head has only one node.
            return True

        one, two = head, head
        before = head

        while two and two.next:
            before = one
            one = one.next
            two = two.next.next
        else:
            if two:  # is not None:
                # head has odd nodes.
                # one is center node so that doesn't matter whatever it is.
                one = one.next

        before.next = None

        # reverse one.
        # reverse linked list.
        prev, next = None, None
        while one:
            next = one.next
            one.next = prev
            prev = one
            one = next

        def traverse(first, second) -> bool:
            if first is None or second is None:
                return (first == second == None)
            elif first.val == second.val:
                return traverse(first.next, second.next)
            else:
                return False

        return traverse(prev, head)

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         v = []
#         curr = head
#         while curr:
#             v.append(curr.val)
#             curr = curr.next
#         if v == v[::-1]:
#             return True
#         else:
#             return False

# class Solution:
#     def isPalindrome(self, head: Optional['ListNode']) -> bool:
#         # if just one node,
#         if head.next is None:
#             return True
#
#         one, two = head, head
#         first_history = []
#         second_history = []
#
#         while two and two.next:
#             first_history.append(one.val)
#             one = one.next
#             two = two.next.next
#
#         # one is somewhere else middle (odd case) or one next of middle (even case)
#         while one:
#             second_history.append(one.val)
#             one = one.next
#
#         if len(first_history) == len(second_history) and \
#                 first_history[::-1] == second_history:
#             return True
#         else:
#             second_history.pop(0)
#             if first_history[::-1] == second_history:
#                 return True
#             else:
#                 return False
