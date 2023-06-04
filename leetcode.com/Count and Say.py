"""
https://leetcode.com/problems/count-and-say/
Count and Say
"""


def get_(n: int) -> str:
    if n == 1:
        return '1'

    before = get_(n - 1)
    result = ''

    while before:
        left, right = 0, 0
        while right < len(before):
            # Don't move left
            if before[right] == before[left]:
                right += 1
            else:
                break
        count = right - left
        result += f'{count}{before[left]}'
        before = before[count:]
    return result


class Solution:
    def countAndSay(self, n: int) -> str:
        return get_(n)


s = Solution()
assert s.countAndSay(5) == "111221"
assert s.countAndSay(4) == "1211"
