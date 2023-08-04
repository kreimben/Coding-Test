"""
Sort an array of 0s, 1s and 2s
https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
"""


class Solution:
    def sort012(self, arr, n):
        # arr.sort() # no, just kidding :)
        zero_index = 0  # last zero index in sorted order.
        two_index = len(arr) - 1  # first two index in sorted order.

        # zero
        for index in range(len(arr)):
            if arr[index] == 0:
                arr[zero_index], arr[index] = arr[index], arr[zero_index]
                zero_index += 1

        # two
        for index in range(len(arr) - 1, -1, -1):
            if arr[index] == 2:
                arr[two_index], arr[index] = arr[index], arr[two_index]
                two_index -= 1

        return arr


s = Solution()
assert s.sort012([0, 2, 1, 2, 0], 5) == [0, 0, 1, 2, 2]
assert s.sort012([1, 2, 0, 2, 0], 5) == [0, 0, 1, 2, 2]
