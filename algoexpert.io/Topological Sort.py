"""
Topological Sort
https://www.algoexpert.io/questions/topological-sort
"""
from collections import defaultdict


def topologicalSort(jobs, deps):
    graph = defaultdict(list)

    # loop first and make graph.
    for dep, tar in deps:
        graph[dep].append(tar)

    # if not listed in deps, just loop. (defaultdict)
    for job in jobs:
        graph[job]

    # sort `jobs` according to graph.
    visited = set()
    curr = []

    def dfs(dep) -> bool:
        nonlocal graph, visited, curr
        for n in graph[dep] if dep in graph else []:
            if n not in visited:
                visited.add(n)
                curr.append(dep)
                res = dfs(n)
                curr.remove(dep)
                if not res:
                    return res
            elif n in curr:
                return False
        jobs.append(dep)
        jobs.remove(dep)
        return True

    for key in graph.keys():
        if key not in visited:
            visited.add(key)
            res = dfs(key)
            if not res:
                return []

    return jobs[::-1]


# assert topologicalSort([1, 2, 3, 4, 5], [[1, 4], [5, 2]]) == [5, 2, 3, 1, 4]
# assert topologicalSort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]) == [1, 4, 3, 2]
assert topologicalSort([1, 2, 3, 4, 5, 6, 7, 8], [
    [3, 1],
    [8, 1],
    [8, 7],
    [5, 7],
    [5, 2],
    [1, 4],
    [1, 6],
    [1, 2],
    [7, 6],
    [4, 6],
    [6, 2],
    [2, 3]
]) == []
