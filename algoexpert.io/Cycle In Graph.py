"""
https://www.algoexpert.io/questions/cycle-in-graph
Cycle In Graph
"""


def cycleInGraph(edges):
    def dfs(curr_index, visited):
        next_edges = edges[curr_index]
        if next_edges:
            for next_index in next_edges:
                if next_index not in visited:
                    result = dfs(next_index, visited + [next_index])
                    if result:
                        return result
                    else:
                        continue
                else:
                    # visited
                    return True
        return False

    for i in range(len(edges)):
        if edges[i]:
            if dfs(i, [i]):
                return True
            else:
                continue
    return False


assert cycleInGraph([
    [1, 2],
    [2],
    []
]) == False
