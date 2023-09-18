"""
https://neetcode.io/problems/singlyLinkedList
Design Singly Linked List
"""


class LinkedList:

    def __init__(self):
        self._list = []

    def get(self, index: int) -> int:
        return self._list[index] if index < len(self._list) else -1

    def insertHead(self, val: int) -> None:
        self._list = [val] + self._list

    def insertTail(self, val: int) -> None:
        self._list.append(val)

    def remove(self, index: int) -> bool:
        if not (0 <= index < len(self._list)):
            return False
        else:
            self._list.pop(index)
            return True

    def getValues(self) -> [int]:
        return self._list
