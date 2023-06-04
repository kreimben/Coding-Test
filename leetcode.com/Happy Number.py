"""
https://leetcode.com/problems/happy-number/
Happy Number
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        MAX_TRY = 500

        count = 0
        while count <= MAX_TRY:
            if n == 1:
                break
            # print(f'current {n=}')
            count += 1
            res = []
            for num in str(n):
                res.append(int(num) ** 2)
            n = sum(res)

        # print(f'final {count=} {n=}')
        if count <= MAX_TRY and n == 1:
            return True
        else:
            return False
