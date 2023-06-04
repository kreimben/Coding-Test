"""
https://www.algoexpert.io/questions/shift-linked-list
Shift Linked List
"""


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'


def shiftLinkedList(head, k):
    if k > 0:  # If positive
        # Move tail node to head.
        while k != 0:
            tail_prev = head
            while tail_prev.next.next:
                tail_prev = tail_prev.next
            tail = tail_prev.next
            tail_prev.next = None

            tail.next = head
            head = tail
            k -= 1


    elif k < 0:  # If negative
        # Move head node to tail.
        while k != 0:
            tail = head
            while tail.next:
                tail = tail.next
            tail.next = head
            tail = tail.next
            head = head.next
            tail.next = None
            k += 1

    return head


# def shiftLinkedList(head, k):
#     """
#     This is reconstructive way.
#     O(n) time complexity.
#     """
#
#     list = []
#
#     curr = head
#     while curr:
#         list.append(curr.value)
#         curr = curr.next
#
#     if k > 0:  # move tail node to head.
#         while k != 0:
#             list.insert(0, list.pop())
#             k -= 1
#     else:  # move head node to tail.
#         while k != 0:
#             list.append(list.pop(0))
#             k += 1
#
#     # And reconstruct nodes.
#     root = LinkedList(list.pop(0))
#     curr = root
#     while list:
#         curr.next = LinkedList(list.pop(0))
#         curr = curr.next
#
#     return root


############### For test
def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)
result = shiftLinkedList(head, 2)
array = linkedListToArray(result)

expected = [4, 5, 0, 1, 2, 3]
