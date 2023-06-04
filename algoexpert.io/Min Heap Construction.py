"""
https://www.algoexpert.io/questions/min-heap-construction
Min Heap Construction
"""


class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        while True:
            changed = False
            for parent_index in range(len(array)):
                left_child_index = parent_index * 2 + 1
                right_child_index = left_child_index + 1

                if left_child_index < len(array) and array[parent_index] > array[left_child_index]:
                    array[parent_index], array[left_child_index] = array[left_child_index], array[parent_index]
                    changed = True

                if right_child_index < len(array) and array[parent_index] > array[right_child_index]:
                    array[parent_index], array[right_child_index] = array[right_child_index], array[parent_index]
                    changed = True

            if not changed:
                break
        return array

    def siftDown(self):
        # Write your code here.
        pass

    def siftUp(self):
        # Write your code here.
        pass

    def peek(self):
        return self.heap[0]

    def remove(self):
        result = self.heap.pop(0)
        self.heap = self.buildHeap(self.heap)
        return result

    def insert(self, value):
        self.heap.append(value)
        self.heap = self.buildHeap(self.heap)
