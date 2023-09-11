"""
Word Search II
https://leetcode.com/problems/word-search-ii/
"""


class Solution:
    def findWords(self, board, words):
        # Set Trie
        # The reason I use Trie is for searching word in any position.
        # What if I search EACH word starting from scratch?
        # That way will consume many times.
        d = {}

        for word in words:
            curr = d
            for ch in word:
                if curr.get(ch) is None:
                    curr[ch] = {}
                curr = curr[ch]
            curr['*'] = word

        def is_valid(i, j) -> bool:
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        res = []

        def backtracking(x, y, parent):
            nonlocal res

            curr = parent[board[x][y]]
            if word := curr.pop('*', False):
                res.append(word)

            letter = board[x][y]
            board[x][y] = '#'  # mark it as "visited"

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i, j = x + dx, y + dy

                if is_valid(i, j) and board[i][j] in curr.keys():
                    backtracking(i, j, curr)

            board[x][y] = letter  # recovery
            if not curr: parent.pop(letter)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in d.keys():
                    # go for it.
                    backtracking(i, j, d)

        return list(set(res))


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
assert s.findWords([["b"], ["a"], ["b"], ["b"], ["a"]], ["baa", "abba", "baab", "aba"]) == ["abba"]
assert s.findWords([["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]],
                   ["oa", "oaa"]) == ["oa", "oaa"]
assert s.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                   words=["oath", "pea", "eat", "rain"]) == ["oath", "eat"]
