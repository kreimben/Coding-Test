"""
https://www.algoexpert.io/questions/linked-list-construction
Linked List Construction
"""


# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value} ({self.prev=} / {self.next=})'

    @property
    def is_standalone(self):
        return not (self.prev or self.next)


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node: Node):
        if not node.is_standalone:
            prev = node.prev
            next = node.next

            if prev:
                prev.next = next
            else:
                self.head = next
            if next:
                next.prev = prev
            else:
                self.tail = prev

            node.prev = None
            node.next = None

        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = self.head.prev
        else:
            self.head = node
            self.tail = node

    def setTail(self, node: Node):
        if not node.is_standalone:
            prev = node.prev
            next = node.next

            if prev:
                prev.next = next
            else:
                self.head = next
            if next:
                next.prev = prev
            else:
                self.tail = prev

            node.prev = None
            node.next = None

        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        else:
            self.head = node
            self.tail = node

    def insertBefore(self, node: Node, nodeToInsert: Node):
        if not nodeToInsert.is_standalone:
            prev = nodeToInsert.prev
            next = nodeToInsert.next

            if prev:
                prev.next = next
            else:
                self.head = next
            if next:
                next.prev = prev
            else:
                self.tail = prev

            nodeToInsert.prev = None
            nodeToInsert.next = None

        prev = node.prev
        if prev:
            prev.next = nodeToInsert
        else:  # Because that means node is head.
            self.head = nodeToInsert
        nodeToInsert.prev = prev
        nodeToInsert.next = node
        node.prev = nodeToInsert

    def insertAfter(self, node: Node, nodeToInsert: Node):
        if not nodeToInsert.is_standalone:
            prev = nodeToInsert.prev
            next = nodeToInsert.next

            if prev:
                prev.next = next
            else:
                self.head = next
            if next:
                next.prev = prev
            else:
                self.tail = prev

            nodeToInsert.prev = None
            nodeToInsert.next = None

        next = node.next
        if next:
            next.prev = nodeToInsert
        else:  # Because that means node is tail.
            self.tail = nodeToInsert
        nodeToInsert.next = next
        nodeToInsert.prev = node
        node.next = nodeToInsert

    def insertAtPosition(self, position: int, nodeToInsert: Node):
        if not nodeToInsert.is_standalone:
            prev = nodeToInsert.prev
            next = nodeToInsert.next

            if prev:
                prev.next = next
            else:
                self.head = next
            if next:
                next.prev = prev
            else:
                self.tail = prev

            nodeToInsert.prev = None
            nodeToInsert.next = None
        elif self.head is None and self.tail is None:
            self.head = nodeToInsert
            self.tail = nodeToInsert
            nodeToInsert.next = None
            nodeToInsert.prev = None
            return

        position -= 1
        curr = self.head
        while curr and position > 1:
            print(curr)
            curr = curr.next
            position -= 1

        # Insert `nodeToInsert` right before `curr`.
        prev = curr.prev
        if prev:
            prev.next = nodeToInsert
        nodeToInsert.next = curr
        nodeToInsert.prev = prev
        curr.prev = nodeToInsert
        if self.head == curr:
            self.head = nodeToInsert

    def removeNodesWithValue(self, value: int):  # Remove all of that value.
        curr = self.head
        while curr:
            if curr.value == value:
                prev = curr.prev
                next = curr.next

                if prev:
                    prev.next = next
                else:  # Means curr is head
                    self.head = next
                if next:
                    next.prev = prev
                else:  # Means curr is tail
                    self.tail = prev

            curr = curr.next

    def remove(self, node: Node):
        curr = self.head
        while curr:
            if curr == node:
                prev = node.prev
                next = node.next

                if prev:
                    prev.next = next
                else:  # Which means curr is head.
                    self.head = next
                if next:
                    next.prev = prev
                else:  # Which means curr is prev.
                    self.tail = prev
                break
            else:
                curr = curr.next

    def containsNodeWithValue(self, value: int):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne


case1 = DoublyLinkedList()
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
bindNodes(one, two)
bindNodes(two, three)
bindNodes(three, four)
case1.head = one
case1.tail = four
assert getNodeValuesHeadToTail(case1) == [1, 2, 3, 4]
assert getNodeValuesTailToHead(case1) == [4, 3, 2, 1]

case1.setTail(one)
assert getNodeValuesHeadToTail(case1) == [2, 3, 4, 1]
assert getNodeValuesTailToHead(case1) == [1, 4, 3, 2]

linkedList = DoublyLinkedList()
one = Node(1)
two = Node(2)
three = Node(3)
three2 = Node(3)
three3 = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
bindNodes(one, two)
bindNodes(two, three)
bindNodes(three, four)
bindNodes(four, five)
linkedList.head = one
linkedList.tail = five

linkedList.setHead(four)
assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 5]
assert getNodeValuesTailToHead(linkedList) == [5, 3, 2, 1, 4]

linkedList.setTail(six)
assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 5, 6]
assert getNodeValuesTailToHead(linkedList) == [6, 5, 3, 2, 1, 4]

linkedList.insertBefore(six, three)
assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 3, 6]
assert getNodeValuesTailToHead(linkedList) == [6, 3, 5, 2, 1, 4]

linkedList.insertAfter(six, three2)
assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 3, 6, 3]
assert getNodeValuesTailToHead(linkedList) == [3, 6, 3, 5, 2, 1, 4]

linkedList.insertAtPosition(1, three3)
assert getNodeValuesHeadToTail(linkedList) == [3, 4, 1, 2, 5, 3, 6, 3]
assert getNodeValuesTailToHead(linkedList) == [3, 6, 3, 5, 2, 1, 4, 3]

linkedList.removeNodesWithValue(3)
assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 6]
assert getNodeValuesTailToHead(linkedList) == [6, 5, 2, 1, 4]

linkedList.remove(two)
assert getNodeValuesHeadToTail(linkedList) == [4, 1, 5, 6]
assert getNodeValuesTailToHead(linkedList) == [6, 5, 1, 4]

assert linkedList.containsNodeWithValue(5) == True
