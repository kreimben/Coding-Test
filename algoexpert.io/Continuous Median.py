"""
https://www.algoexpert.io/questions/continuous-median
Continuous Median
"""
import heapq


# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.


class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.greater_heap = []  # Min Heap
        self.lower_heap = []  # Max Heap

    def insert(self, number):
        if len(self.greater_heap) == len(self.lower_heap) == 0:
            heapq.heappush(self.lower_heap, (-number, number))
        elif self.lower_heap[0][1] < number:
            heapq.heappush(self.greater_heap, number)
        else:
            heapq.heappush(self.lower_heap, (-number, number))

        # Re-balance it.
        if len(self.greater_heap) > 0 and len(self.lower_heap) > 0:
            if len(self.greater_heap) > len(self.lower_heap) + 1:
                target = heapq.heappop(self.greater_heap)
                heapq.heappush(self.lower_heap, (-target, target))
            elif len(self.greater_heap) + 1 < len(self.lower_heap):
                target = heapq.heappop(self.lower_heap)[1]
                heapq.heappush(self.greater_heap, target)

        if len(self.greater_heap + self.lower_heap) % 2 == 0:  # Total saved node's count is even number.
            self.median = (self.greater_heap[0] + self.lower_heap[0][1]) / 2
        else:
            self.median = self.lower_heap[0][1] if len(self.lower_heap) > len(self.greater_heap) else self.greater_heap[
                0]

    def getMedian(self):
        return self.median


handler = ContinuousMedianHandler()
handler.insert(5)
handler.insert(10)
assert handler.getMedian() == 7.5
handler.insert(100)
assert handler.getMedian() == 10
handler.insert(200)
assert handler.getMedian() == 55
