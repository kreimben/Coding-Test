"""
https://leetcode.com/problems/neighboring-bitwise-xor/
Neighboring Bitwise XOR
"""
from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        N = len(derived)
        original = [None] * N
        if N == 1:
            if derived[0] == 0:
                return True
            else:
                return False

        for i, num in enumerate(derived):
            curr = original[i]
            counterpart = original[(i + 1) % N]
            next_index = (i + 1) % N

            if derived[i] == 1:
                # curr and counterpart should be different!
                if curr is None and counterpart is None:
                    original[i] = 0
                    original[(i + 1) % N] = 1
                elif curr == 0 and counterpart != 0:
                    original[(i + 1) % N] = 1
                elif curr == 1 and counterpart != 1:
                    original[(i + 1) % N] = 0
                elif counterpart == 0 and curr != 0:
                    original[i] = 0
                elif counterpart == 1 and curr != 1:
                    original[i] = 1
                else:
                    return False
            else:
                # curr and counterpart should be same!
                if curr is None and counterpart is None:
                    original[i] = 0
                    original[(i + 1) % N] = 0
                elif curr == 0 and counterpart != 1:
                    original[(i + 1) % N] = 0
                elif curr == 1 and counterpart != 0:
                    original[(i + 1) % N] = 1
                elif counterpart == 0 and curr != 1:
                    original[i] = 0
                elif counterpart == 1 and curr != 0:
                    original[i] = 1
                else:
                    return False
        return True
