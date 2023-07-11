"""
https://leetcode.com/problems/rotting-oranges/description/
Rotting Oranges
"""


class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        def check_if_fresh_exist(grid: [[int]]) -> int:
            res = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        res += 1
            return res

        number_of_one = check_if_fresh_exist(grid)

        # if there are no 2, return -1
        def check_two_and_one():
            val = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        return 2
                    elif grid[i][j] == 1:
                        val = 1
            return val

        if (val := check_two_and_one()) == 0:
            return 0
        elif val == 1:
            return -1

        # before going to main judgement, I have to find if there is any isolated orange.
        # and if existed, return -1
        def ivr(i, j) -> bool:
            """
            is_valid_range
            """
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return True
            else:
                return False

        case = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        )

        # BFS
        maxtime = 0
        visited = set()

        status = 0  # 0==really end, 1==there are isolated 1

        def bfs(level: int, twos: tuple):
            nonlocal case, visited, maxtime, status, number_of_one
            # There should be multiple initial rotten orange.
            if number_of_one == 0:
                return  # no more compute.
            elif len(twos) == 0:
                status = 1
                return
            # twos are next search target.
            new_twos = []
            for i, j in twos:
                for di, dj in case:
                    x, y = i + di, j + dj
                    if ivr(x, y) and grid[x][y] == 1 and (x, y) not in visited:
                        visited.add((x, y))
                        new_twos.append((x, y))

            for i, j in new_twos:
                grid[i][j] = 2
                number_of_one -= 1

            maxtime = max(maxtime, level)
            bfs(level + 1, tuple(new_twos))

        twos = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    twos.append((i, j))
                    visited.add((i, j))
        bfs(1, tuple(twos))

        return maxtime if status == 0 else -1
