"""
https://www.algoexpert.io/questions/remove-kth-node-from-end
Remove Kth Node From End
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


def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next:
        second = second.next
        first = first.next
    first.next = first.next.next


# ===========
import unittest


class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = LinkedList(1).addMany([2, 3, 4, 5, 6, 7, 8, 9])
        removeKthNodeFromEnd(test, 10)
        self.assertEqual(expected.getNodesInArray(), test.getNodesInArray())


t = TestProgram()
t.test_case_1()
