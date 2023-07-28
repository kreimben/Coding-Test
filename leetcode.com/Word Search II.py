"""
Word Search II
https://leetcode.com/problems/word-search-ii/
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.refs = 0

    def add_word(self, word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1
        curr.is_word = True

    def remove_word(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                    r not in range(ROWS)
                    or c not in range(COLS)
                    or board[r][c] not in node.children
                    or node.children[board[r][c]].refs < 1
                    or (r, c) in visit
            ):
                return

            # backtracking!
            visit.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                node.is_word = False
                res.add(word)
                root.remove_word(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # backtracking!
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         """
#         pure dfs and time limit exceeded
#         """
#
#         # I should assume that every characters in `board` are NOT UNIQUE.
#         def is_valid(x: int, y: int) -> bool:
#             return 0 <= x < len(board) and 0 <= y < len(board[0])
#
#         case = (
#             (0, 1),
#             (0, -1),
#             (1, 0),
#             (-1, 0)
#         )
#         res = set()
#         words.sort(key=lambda x: len(x), reverse=True)
#
#         def dfs(x: int, y: int, word: str, stack: [tuple]):
#             nonlocal case, res
#             if not words:
#                 return
#             elif len(word) > len(words[0]):
#                 return
#             elif word in words:
#                 res.add(word)
#                 words.remove(word)
#                 words.sort(key=lambda x: len(x), reverse=True)
#
#             for dx, dy in case:
#                 i, j = x + dx, y + dy
#                 if is_valid(i, j) and (i, j) not in stack:
#                     dfs(i, j, word + board[i][j], stack + [(i, j)])
#
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 dfs(i, j, board[i][j], [(i, j)])
#
#         return list(res)


s = Solution()
# assert s.findWords([["b"], ["a"], ["b"], ["b"], ["a"]], ["baa", "abba", "baab", "aba"]) == ["abba"]
# assert s.findWords([["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]],
#                    ["oa", "oaa"]) == ["oa", "oaa"]
assert s.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                   words=["oath", "pea", "eat", "rain"]) == ["oath", "eat"]
