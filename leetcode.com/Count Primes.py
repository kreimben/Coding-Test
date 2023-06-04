"""
https://leetcode.com/problems/count-primes/
Count Primes
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        d = {}

        def is_prime(n: int):
            if n == 2:
                return True
            elif n == 1:
                return False
            for i in range(2, n - 1):
                if n % i == 0:
                    return False
            return True

        count = 0
        for i in range(1, n):
            if (v := d.get(i)) is not None:
                if v:
                    count += 1
            else:
                d[i] = is_prime(i)
                if d[i] is True:
                    count += 1
        return count


s = Solution()
assert s.countPrimes(10) == 4
