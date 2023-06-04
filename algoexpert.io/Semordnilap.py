"""
https://www.algoexpert.io/questions/semordnilap
Semordnilap
"""
from collections import defaultdict


def semordnilap(words: [str]) -> []:
    results = []

    d = defaultdict(list[str])
    while words:
        word = words.pop()
        d[len(word)].append(word)

    for key, value in d.items():
        while value:
            word = value.pop()
            a = word
            b = word[::-1]
            if word[::-1] in value:
                result = [word, word[::-1]]
                results.append(result)
                value.remove(word[::-1])

    return results


assert semordnilap(["dog", "desserts", "god", "stressed"]) == [['dog', 'god'], ['desserts', 'stressed']]
