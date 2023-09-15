"""
Design Dynamic Array (Resizable Array)
https://neetcode.io/problems/dynamicArray
"""


class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._list = []

    def get(self, i: int) -> int:
        return self._list[i]

    def insert(self, i: int, n: int) -> None:
        self._list[i] = n

    def pushback(self, n: int) -> None:
        self._list.append(n)
        while len(self._list) > self.capacity:
            self.resize()

    def popback(self) -> int:
        return self._list.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self._list)

    def getCapacity(self) -> int:
        return self.capacity
