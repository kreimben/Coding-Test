"""
https://www.algoexpert.io/questions/group-anagrams
Group Anagrams
"""


def groupAnagrams(words):
    # First, store sorted string with index.
    group = [
        (i, ''.join(sorted(s)))
        for i, s in enumerate(words)
    ]
    # sor is non-duplicated and sorted array of words.
    sor = list(set([''.join(sorted(s)) for s in words]))
    results = []

    while sor:
        word = sor.pop()
        temp = []
        for i, s in group:
            if s == word:
                temp.append(words[i])
        results.append(temp)

    return results
