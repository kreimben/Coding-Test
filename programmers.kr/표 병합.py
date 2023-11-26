"""
표 병합
https://school.programmers.co.kr/learn/courses/30/lessons/150366
"""


def solution(commands):
    COMMAND = ['UPDATE', 'MERGE', 'UNMERGE', 'PRINT']
    EMPTY = 'EMPTY'

    chart = [[(j, i) for i in range(51)] for j in range(51)]  # table[(r, c)] = parent value.
    values = [[EMPTY for _ in range(51)] for _ in range(51)]  # table[(r, c)] = value.

    def find(p: (int, int)) -> (int, int):
        if chart[p[0]][p[1]] == p:
            return chart[p[0]][p[1]]
        else:
            return find(chart[p[0]][p[1]])

    def union(p: (int, int), c: (int, int)):
        parent = find(p)
        child = find(c)
        chart[child[0]][child[1]] = parent

    res = []
    for command in commands:
        cmd = command.split()
        if cmd[0] == COMMAND[0] and len(cmd) == 4:  # 'UPDATE' value in (r, c).
            r, c, v = int(cmd[1]), int(cmd[2]), cmd[3]
            R, C = find((r, c))
            values[R][C] = v
        elif cmd[0] == COMMAND[0] and len(cmd) == 3:  # 'UPDATE' all values like cmd[2].
            for i in range(50):
                for j in range(50):
                    R, C = find((i, j))
                    values[R][C] = cmd[2]
        elif cmd[0] == COMMAND[1]:  # MERGE
            r1, c1, r2, c2 = int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4])
            union((r1, c1), (r2, c2))
        elif cmd[0] == COMMAND[2]:  # UNMERGE
            r, c = int(cmd[1]), int(cmd[2])
            chart[r][c] = find((r, c))
        elif cmd[0] == COMMAND[3]:  # PRINT
            r, c = int(cmd[1]), int(cmd[2])
            res.append(values[r][c])
    return res


assert solution(
    ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice",
     "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta",
     "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik",
     "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
) == ["EMPTY", "group"]
