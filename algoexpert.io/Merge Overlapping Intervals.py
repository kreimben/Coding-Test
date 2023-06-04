"""
https://www.algoexpert.io/questions/merge-overlapping-intervals
Merge Overlapping Intervals
"""


def mergeOverlappingIntervals(intervals: [[int]]):
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        left, right = i, i + 1
        while right < len(intervals):
            lstart = intervals[left][0]
            lend = intervals[left][1]

            rstart = intervals[right][0]
            rend = intervals[right][1]

            if lend >= rstart:  # then merge it!
                new = [min(lstart, rstart), max(lend, rend)]
                intervals.append(new)
                intervals.pop(right)
                intervals.pop(left)
                intervals.sort(key=lambda x: x[0])
            elif lend < rstart:  # Just pass this case.
                break
            else:
                right += 1

    return intervals


assert mergeOverlappingIntervals([
    [20, 21],
    [22, 23],
    [0, 1],
    [3, 4],
    [23, 24],
    [25, 27],
    [5, 6],
    [7, 19]
]) == [[0, 1],
       [3, 4],
       [5, 6],
       [7, 19],
       [20, 21],
       [22, 24],
       [25, 27]]
assert mergeOverlappingIntervals([
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
    [1, 10]
]) == [[1, 10]]
assert mergeOverlappingIntervals([
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
]) == [[1, 2], [3, 8], [9, 10]]
