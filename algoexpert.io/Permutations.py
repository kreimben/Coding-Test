"""
https://www.algoexpert.io/questions/permutations
Permutations
"""


def getPermutations(array: [int]):
    # Use DFS!
    # Every element is UNIQUE!
    results = []
    if not array:
        return results

    def dfs(given: [int]):
        if len(given) == len(array):
            results.append(given)
        else:
            for num in array:
                if num not in given:
                    dfs(given + [num])

    dfs([])

    return results


assert getPermutations([]) == []
assert getPermutations([1, 2, 3]) == [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]
