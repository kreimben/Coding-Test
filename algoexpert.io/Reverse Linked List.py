"""
https://www.algoexpert.io/questions/reverse-linked-list
Reverse Linked List
"""


# image for helping understanding
# https://storage.googleapis.com/algodailyrandomassets/tutorials-optimized/reverse-a-linked-list-image-cover.png

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    curr = head
    prev = None
    while curr:
        next = curr.next  # back up next element for next loop
        curr.next = prev  # set next element as prev
        prev = curr  # set prev as curr for next loop
        curr = next  # skip for next loop
    return prev
