"""
https://leetcode.com/problems/sliding-window-maximum/
Sliding Window Maximum
"""

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         # O(n log n)
#         res = []
#         heap = []  # max heap
#
#         # set the block
#         for i in range(len(nums)):
#             if len(heap) == k:
#                 res.append(heap[0][1])
#                 heap.remove((-nums[i - k], nums[i - k]))
#                 heapq.heapify(heap)
#             heapq.heappush(heap, (-nums[i], nums[i]))
#         res.append(heap[0][1])
#
#         return res


s = Solution()
assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
