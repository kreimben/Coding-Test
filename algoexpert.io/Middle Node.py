"""
https://www.algoexpert.io/questions/middle-node
Middle Node
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(node: LinkedList):
    one, two = node, node
    while two and two.next:
        one = one.next
        two = two.next.next
    return one
