"""
https://www.algoexpert.io/questions/sum-of-linked-lists
Sum of Linked Lists
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    def list_to_int(ll):
        s = []
        curr = ll
        while curr:
            s.append(str(curr.value))
            curr = curr.next
        return int(''.join(reversed(s)))

    one = list_to_int(linkedListOne)
    two = list_to_int(linkedListTwo)
    r = one + two  # int value => r = 2291

    l = list(reversed(list(str(r))))
    head = LinkedList(int(l.pop(0)))
    curr = head
    for val in l:  # val => 1 => 9 => 2 => 2
        curr.next = LinkedList(int(val))
        curr = curr.next

    return head


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!


import unittest


class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        ll1 = LinkedList(2).addMany([4, 7, 1])
        ll2 = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = sumOfLinkedLists(ll1, ll2)
        self.assertEqual(getNodesInArray(actual), getNodesInArray(expected))
