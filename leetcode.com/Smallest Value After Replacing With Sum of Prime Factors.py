"""
https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/
Smallest Value After Replacing With Sum of Prime Factors
"""


class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            if n == 4:
                return n
            temp = []
            able_to_pass = True

            while n != 1:
                is_prime = True
                for i in range(2, n):
                    if n % i == 0:
                        is_prime = False
                        n //= i
                        able_to_pass = False
                        temp.append(i)
                        break
                if is_prime:
                    temp.append(n)
                    n = 1

            n = sum(temp) if temp else n

            if able_to_pass:
                break

        return n


s = Solution()
assert s.smallestValue(9) == 5
assert s.smallestValue(4) == 4
assert s.smallestValue(15) == 5
