"""
https://www.algoexpert.io/questions/two-colorable
Two-Colorable
"""


def twoColorable(edges):
    colors = [None] * len(edges)
    for i in range(len(edges)):
        if i == 0:
            colors[i] = 1

        curr_color = colors[i]
        if curr_color is not None:
            for neighbour in edges[i]:
                if colors[neighbour]:
                    if colors[neighbour] == curr_color:
                        # That can't be possible.
                        return False
                else:
                    colors[neighbour] = 1 if curr_color != 1 else 0
        else:  # curr color is none
            adjacent = None
            for edge in edges[i]:
                if edge is not None:
                    adjacent = edge
                    break
            colors[i] = (colors[adjacent] + 1) % 2

    return True


assert twoColorable([
    [2],
    [2, 3],
    [0, 1],
    [1]
]) == True

assert twoColorable([
    [1],
    [0]
]) == True

assert twoColorable([
    [1, 4],
    [0, 2, 3],
    [1, 4],
    [1],
    [0, 2]
]) == True
