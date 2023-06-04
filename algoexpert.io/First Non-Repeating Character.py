"""
https://www.algoexpert.io/questions/first-non-repeating-character
First Non-Repeating Character
"""


def firstNonRepeatingCharacter(s: str):
    d = {}

    for ch in s:
        if d.get(ch):
            d[ch] += 1
        else:
            d[ch] = 1

    for key, value in d.items():
        if value == 1:
            for i, ch in enumerate(list(s)):
                if ch == key:
                    return i
    return -1


assert firstNonRepeatingCharacter("abcdcaf") == 1
