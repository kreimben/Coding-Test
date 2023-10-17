"""
Letter Tile Possibilities
https://leetcode.com/problems/letter-tile-possibilities/description/
"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        chars = list(tiles)

        stack = []

        def backtracking():
            nonlocal stack, res
            if len(stack) > len(chars):
                return
            elif stack:
                res.add(''.join(tiles[i] for i in stack))
            for i in range(len(tiles)):
                if i in stack: continue
                stack.append(i)
                backtracking()
                stack.pop()

        for i in range(len(tiles)):
            stack.append(i)
            backtracking()
            stack.pop()

        return len(res)
