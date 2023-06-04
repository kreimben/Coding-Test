"""
https://leetcode.com/problems/meeting-rooms-iii/
Meeting Rooms III
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = []
        used = defaultdict(int)

        for start, end in meetings:
            while rooms and rooms[0][0] <= start:
                heapq.heappop(rooms)
            if len(rooms) < n:
                unused = [True for _ in range(n)]
                for _, room in rooms:
                    unused[room] = False
                room = unused.index(True)
                used[room] += 1
                heapq.heappush(rooms, (end, room))
            else:  # len(rooms) == n
                e, last = heapq.heappop(rooms)
                used[last] += 1
                heapq.heappush(rooms, (e + end - start, last))
        heap = []
        for k, v in used.items():
            heapq.heappush(heap, (-v, k))
        return heap[0][1]


s = Solution()
assert s.mostBooked(4, [[48, 49], [22, 30], [13, 31], [31, 46], [37, 46], [32, 36], [25, 36], [49, 50], [24, 34],
                        [6, 41]]) == 0
assert s.mostBooked(2, [[0, 10], [1, 2], [12, 14], [13, 15]]) == 0
assert s.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1
