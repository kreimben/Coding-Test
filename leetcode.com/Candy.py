"""
Candy
https://leetcode.com/problems/candy/description/
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candy = [1] * N

        for i in range(1, N):
            if ratings[i - 1] < ratings[i]:
                candy[i] = max(candy[i - 1] + 1, candy[i])

        for i in range(N - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                candy[i] = max(candy[i + 1] + 1, candy[i])

        return sum(candy)
