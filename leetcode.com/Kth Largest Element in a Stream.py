"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
Kth Largest Element in a Stream
"""


class KthLargest:
    k: int
    kth_element: int | None = None
    q: [int]

    def __init__(self, k: int, nums: [int]):
        self.q = []
        for num in nums:
            self.q.append(num)
        self.q.sort()
        self.k = k

    def add(self, val: int) -> int:
        self.q.append(val)
        self.q.sort()
        self.kth_element = self.q[-self.k]
        return self.kth_element


k = KthLargest(3, [4, 5, 8, 2])
assert k.add(3) == 4
assert k.add(5) == 5
assert k.add(10) == 5
assert k.add(9) == 8
assert k.add(4) == 8
