"""
https://www.algoexpert.io/questions/common-characters
Common Characters
"""
from collections import defaultdict


def commonCharacters(strings):
    note = [0] * 256
    res = []

    for s in strings:
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        for key in d.keys():
            note[ord(key)] += 1

    for i, val in enumerate(note):
        if val == len(strings):
            res.append(chr(i))

    return res
