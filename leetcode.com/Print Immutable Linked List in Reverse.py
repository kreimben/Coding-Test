"""
Print Immutable Linked List in Reverse
https://leetcode.com/problems/print-immutable-linked-list-in-reverse/
"""


# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        def print_node(node) -> None:
            next = node.getNext()
            if next:
                print_node(next)
            node.printValue()

        print_node(head)
