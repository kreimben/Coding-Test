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

    # sort `jobs` according to graph.
    visited = set()

    def dfs(dep):
        nonlocal graph, visited
        for n in graph[dep] if dep in graph else []:
            if n not in visited:
                visited.add(n)
                dfs(n)
        # res.append(dep)
        jobs.append(dep)
        jobs.remove(dep)

    for key in graph.keys():
        if key not in visited:
            visited.add(key)
            dfs(key)

    return jobs[::-1] if not graph else []


# def topologicalSort(jobs, deps):
#     res = jobs.copy()
#     HAS_CHANGED = False
#
#     def judge(dep, target):
#         nonlocal res, HAS_CHANGED
#         if dep in res and target in res and res.index(dep) > res.index(target):
#             # then swap them.
#             di, ti = res.index(dep), res.index(target)
#             res[di], res[ti] = res[ti], res[di]
#             HAS_CHANGED = True
#         elif dep in res and target not in res:
#             # then just append
#             res.append(target)
#             HAS_CHANGED = True
#         elif target in res and dep not in res:
#             # then insert dependency in front of target.
#             ti = res.index(target)
#             res.insert(ti, dep)
#             HAS_CHANGED = True
#         elif dep not in res and target not in res:
#             # if dep and target is not in `res`.
#             res.append(dep)
#             res.append(target)
#             HAS_CHANGED = True
#
#     CALLENGE_LIMIT = 5
#     i = 0
#     while i <= CALLENGE_LIMIT:
#         for dep, tar in deps:
#             judge(dep, tar)
#         if not HAS_CHANGED:
#             break
#         i += 1
#         HAS_CHANGED = False
#
#     return res if i <= CALLENGE_LIMIT else []


assert topologicalSort([1, 2, 3, 4, 5], [[1, 4], [5, 2]]) == [5, 2, 3, 1, 4]
assert topologicalSort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]) == [1, 4, 3, 2]
