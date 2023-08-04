"""
Move all negative elements to end
https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1
"""


# class Solution:
#     def segregateElements(self, arr, n):
#         pos = []
#         neg = []
#
#         while arr:
#             val = arr.pop(0)
#             if val < 0:
#                 neg.append(val)
#             else:
#                 pos.append(val)
#         temp = pos + neg
#         for i in range(n):
#             arr.append(temp[i])
#
#         return arr


class Solution:
    def segregateElements(self, arr, n):
        i = 0
        count = 0
        while count < len(arr):
            val = arr[i]
            if val < 0:
                arr.remove(val)
                arr.append(val)
            else:
                i += 1
            count += 1

        return arr


s = Solution()
assert s.segregateElements([1, -1, 3, 2, -7, -5, 11, 6], 8) == [1, 3, 2, 11, 6, -1, -7, -5]
