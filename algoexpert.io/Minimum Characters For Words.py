"""
https://www.algoexpert.io/questions/minimum-characters-for-words
Minimum Characters For Words
"""
from collections import defaultdict


def minimumCharactersForWords(words):
    def count(array, target) -> int:
        count = 0
        for element in array:
            if target == element:
                count += 1
        return count

    results = []
    for word in words:
        d = defaultdict(int)
        for ch in word:
            d[ch] += 1
        for key, value in d.items():
            c = count(results, key)
            if value != c:
                # Need to be fixed.
                results += [key] * (value - c)

    return results


actual = minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"])
expected = ["t", "h", "i", "s", "t", "a", "d", "d", "e", "e", "m", "!"]
assert sorted(actual) == sorted(expected)
