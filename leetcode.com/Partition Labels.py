"""
Partition Labels
https://leetcode.com/problems/partition-labels/description/
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # "ababcbaca"
        # a => 4 / b => 3 / c => 2
        # "defegde"
        # d => 2 / e => 3 / f => 1 / g => 1
        # "hijhklij"
        # h => 2 / i => 2 / j => 2 / k => 1 / l => 1

        # find the first a to last a of index.
        # follow the rest of characters.
        # a => 0 to 8
        # b => 1 to 5
        # c => 4 to 7
        # d => 9 to 14
        # then cut the d

        d = {}
        for i, ch in enumerate(s):
            if ch not in d:
                d[ch] = [i, i]
            else:
                d[ch][1] = i

        # I assume and assert d.keys() keep the order in chars.
        res = []
        curr = []
        for k, (start, end) in d.items():
            if not curr:
                curr = [start, end]
            else:
                if curr[1] < start:
                    # should separate.
                    # if not res: res.append(start)
                    # else: res.append(start - res[-1])
                    res.append(curr[1] - curr[0] + 1)
                    curr = [start, end]
                else:
                    # if not, it's included.
                    curr[0] = min(start, curr[0])
                    curr[1] = max(end, curr[1])
        else:
            res.append(curr[1] - curr[0] + 1)

        return res


class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        intervals = []
        d = {}
        for i, ch in enumerate(s):
            if ch not in d:
                d[ch] = [i, i]
            else:
                d[ch][1] = i

        for _, (start, end) in d.items():
            intervals.append([start, end])

        # merge intervals
        intervals.sort(key=lambda x: x[0])

        while True:
            target = []
            for i in range(1, len(intervals)):
                prev, curr = intervals[i - 1], intervals[i]
                if prev[1] < curr[0]:
                    # not overlapping
                    continue
                else:
                    # overlapping
                    intervals[i][0] = min(prev[0], curr[0])
                    intervals[i][1] = max(prev[1], curr[1])
                    target.append(i - 1)

            if not target: break
            while target:
                intervals.pop(target.pop())

        res = []
        for start, end in intervals:
            res.append(end - start + 1)

        return res


s = Solution()
assert s.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
