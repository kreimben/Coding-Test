"""
https://www.algoexpert.io/questions/remove-duplicates-from-linked-list
Remove Duplicates From Linked List
"""
from collections import defaultdict


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next: LinkedList | None = None

    def addMany(self, values: [int]):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self) -> [int]:
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


def check(linked_list: LinkedList):
    d = defaultdict(int)
    d[linked_list.value] += 1  # cuz it's first time to count duplicates.
    while linked_list.next is not None:
        if d[linked_list.next.value] == 0:
            d[linked_list.next.value] += 1
            linked_list = linked_list.next
        else:
            if linked_list.next.next is not None:
                linked_list.next = linked_list.next.next
            else:
                linked_list.next = None


def removeDuplicatesFromLinkedList(linked_list: LinkedList):
    check(linked_list)
    return linked_list


test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
expected = LinkedList(1).addMany([3, 4, 5, 6])
actual = removeDuplicatesFromLinkedList(test)

assert actual.getNodesInArray() == expected.getNodesInArray()
