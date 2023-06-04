"""
https://leetcode.com/problems/find-median-from-data-stream/
Find Median from Data Stream
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.left = []  # Max Heap for get median value
        self.right = []  # Min Heap for get median value

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heapq.heappush(self.left, (-num, num))
        else:
            heapq.heappush(self.right, num)

        while self.left and self.right and self.left[0][1] > self.right[0]:
            l = heapq.heappop(self.left)[1]
            r = heapq.heappop(self.right)

            heapq.heappush(self.left, (-r, r))
            heapq.heappush(self.right, l)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0][1] + self.right[0]) / 2
        else:
            return self.left[0][1]


# Your MedianFinder object will be instantiated and called as such:
m = MedianFinder()
commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
values = [[], [1], [2], [], [3], []]
outputs = [None, None, None, 1.5, None, 2.0]
actual = []

for i, command in enumerate(commands):
    if command == 'MedianFinder':
        actual.append(None)
    elif command == 'addNum':
        m.addNum(values[i][0])
        actual.append(None)
    elif command == 'findMedian':
        actual.append(m.findMedian())

assert actual == outputs
