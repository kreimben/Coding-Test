"""
https://www.algoexpert.io/questions/merging-linked-lists
Merging Linked Lists
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value} ({self.next})'

    def __repr__(self):
        return f'{self.value} ({self.next})'


def len_(head):
    curr = head
    count = 0
    while curr:
        curr = curr.next
        count += 1
    return count


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # To find intersection of two linked lists, Must traverse.
    start = None
    end = None

    one = linkedListOne
    two = linkedListTwo

    diff = len_(linkedListOne) - len_(linkedListTwo)

    if diff > 0:
        # linked list one is longer
        while diff > 0:
            diff -= 1
            one = one.next

    elif diff < 0:
        # linked list two is longer
        while diff < 0:
            diff += 1
            two = two.next

    for _ in range(min(len_(linkedListOne), len_(linkedListTwo))):
        if one.value == two.value:
            if start is None:
                start = one
            else:
                end = one

        one = one.next
        two = two.next

    if end:
        end.next = None
    return start


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class TestProgram(unittest.TestCase):
    def test_case_2(self):
        l1 = LinkedList(1)

        l2 = LinkedList(2)
        l2.next = LinkedList(3)
        l2.next.next = LinkedList(4)
        l2.next.next.next = LinkedList(1)

        expected = l1
        actual = mergingLinkedLists(l1, l2)
        self.assertEqual(actual, expected)

    def test_case_1(self):
        l1 = LinkedList(1)
        l1.next = LinkedList(2)
        l1.next.next = LinkedList(3)
        l1.next.next.next = LinkedList(4)

        l2 = LinkedList(5)
        l2.next = l1.next.next

        expected = l1.next.next
        actual = mergingLinkedLists(l1, l2)
        self.assertEqual(actual, expected)


t = TestProgram()
t.test_case_2()
t.test_case_1()
