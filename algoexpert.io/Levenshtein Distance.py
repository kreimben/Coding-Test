"""
https://www.algoexpert.io/questions/levenshtein-distance
Levenshtein Distance
"""


def levenshteinDistance(str1, str2):
    results = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for i in range(len(str1) + 1):
        results[i][0] = i

    for i in range(len(str2) + 1):
        results[0][i] = i

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] != str2[j - 1]:
                curr = min(
                    results[i - 1][j],  # up
                    results[i][j - 1],  # left
                    results[i - 1][j - 1]  # up and left
                ) + 1
            else:
                curr = results[i - 1][j - 1]
            results[i][j] = curr

    return results[len(results) - 1][len(results[0]) - 1]


assert levenshteinDistance('abc', 'yabd') == 2
assert levenshteinDistance("gumbo", "gambol") == 2
assert levenshteinDistance('', 'abc') == 3
assert levenshteinDistance("biting", "mitten") == 4
levenshteinDistance("abcdefghij", "a234567890")
