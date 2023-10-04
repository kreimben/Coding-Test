"""
Confusing Number II
https://leetcode.com/problems/confusing-number-ii/
"""


class Solution:
    # concise and clever solution
    def confusingNumberII(self, n: int) -> int:
        pairs = {'1': '1', '0': '0', '6': '9', '9': '6', '8': '8'}
        final = 0

        def backtrack(conf_num: str, original_num: str) -> None:
            nonlocal final

            if original_num != conf_num:
                final += 1

            for i in pairs:
                if int(original_num + i) <= n:
                    backtrack(pairs[i] + conf_num, original_num + i)

        for i in ('1', '6', '9', '8'):
            backtrack(pairs[i], i)

        return final


class Solution:
    # verbose solution
    def confusingNumberII(self, n: int) -> int:
        valid = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        # confusing number is being different number when each digit is rotated.
        def rotate(num: str) -> int:
            nonlocal valid
            res = ''
            for ch in num:
                res = valid[ch] + res
            return int(res)

        stack = []
        count = 0

        def dfs():
            nonlocal stack, n, count
            if int(''.join(stack)) > n:
                return
            else:
                num = ''.join(stack)
                converted = rotate(num)
                if int(num) != converted:
                    count += 1

            for i in range(n + 1 if n < 10 else 10):
                if i in [2, 3, 4, 5, 7]: continue
                stack.append(str(i))
                dfs()
                stack.pop()

        for i in range(1, n + 1 if n < 10 else 10):
            if i in [2, 3, 4, 5, 7]: continue
            stack.append(str(i))
            dfs()
            stack.pop()

        return count
