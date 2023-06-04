"""
https://www.algoexpert.io/questions/longest-palindromic-substring
Longest Palindromic Substring
"""


def longestPalindromicSubstring(string):
    max_len = 0
    ml, mr = 0, 0
    for left in range(len(string)):
        right = len(string)

        while left <= right:
            ready = string[left: right]

            if ready == ready[::-1] and max_len < right - left + 1:
                max_len = right - left + 1
                ml = left
                mr = right
                break

            right -= 1

    return string[ml:mr]


assert longestPalindromicSubstring("abcdefgfedcbazzzzzzzzzzzzzzzzzzzz") == 'zzzzzzzzzzzzzzzzzzzz'
assert longestPalindromicSubstring("abaxyzzyxf") == 'xyzzyx'
