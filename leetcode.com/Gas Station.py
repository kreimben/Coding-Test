"""
Gas Station
https://leetcode.com/problems/gas-station/
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tatal = 0
        curr = 0
        res = 0

        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            tatal += gas[i] - cost[i]
            curr += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if curr < 0:
                curr = 0
                res = i + 1

        return res if tatal >= 0 else -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # what if I merge gas and cost arraies?
        # ex1. [-2, -2, -2, 3, 3]
        # ex2. [-1, -1, 1] => We can't traverse a full course in which any position.
        total = [g - c for g, c in zip(gas, cost)]
        N = len(gas)
        visited = []

        def count(index: int, rest: int) -> bool:
            nonlocal total, N, visited
            # 1. get the balance at the point of (index)th.
            balance = total[index] + rest
            if balance < 0:
                return False

            # 2. should go further. (to the next number)
            calculated_index = (index + 1) % N
            if calculated_index in visited:
                return True
            visited.append(calculated_index)
            res = count(calculated_index, balance)
            visited.pop()

            # 3. return res
            return res

        for i in range(N):
            if total[i] >= 0:
                visited.append(i)
                if count(i, 0): return i
                visited.pop()

        return -1
