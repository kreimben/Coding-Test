"""
Course Schedule
https://leetcode.com/problems/course-schedule/description/
"""
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for tar, dep in prerequisites:
            graph[dep].append(tar)
        for val in range(numCourses):
            graph[val]

        visited = set()
        curr = []

        def dfs(dep):
            nonlocal graph, visited, curr
            for n in graph[dep] if dep in graph else []:
                if n not in visited:
                    visited.add(n)
                    curr.append(n)
                    res = dfs(n)
                    curr.remove(n)
                    if not res: return False  # res
                elif n in curr:
                    return False
            return True

        for key in graph.keys():
            if key not in visited:
                visited.add(key)
                curr.append(key)
                res = dfs(key)
                curr.remove(key)
                if not res: return False  # res

        return True
