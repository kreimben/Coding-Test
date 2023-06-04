"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
Design Add and Search Words Data Structure
"""
from unittest import TestCase


# class WordDictionary:
#     """
#     It's not very efficient code.
#     That's reason to use `trie`.
#     """
#     def __init__(self):
#         self.d = defaultdict(set)
#
#     def addWord(self, word: str) -> None:
#         self.d[len(word)].add(word)
#
#     def search(self, word: str) -> bool:
#         m = len(word)
#         for dict_word in self.d[m]:
#             i = 0
#             while i < m and (dict_word[i] == word[i] or word[i] == '.'):
#                 i += 1
#             if i == m:
#                 return True
#         return False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node

        return search_in_node(word, self.trie)


class Case(TestCase):

    def test1(self):
        commands = ["WordDictionary", "addWord", "addWord", "addWord", "addWord", "search", "search", "addWord",
                    "search", "search", "search", "search", "search", "search"]
        inputs = [[], ["at"], ["and"], ["an"], ["add"], ["a"], [".at"], ["bat"], [".at"], ["an."], ["a.d."], ["b."],
                  ["a.d"], ["."]]

        actual = self.run_with(commands, inputs)
        expected = [None, None, None, None, None, False, False, None, True, True, False, False, True, False]
        # for command, i, a, e in list(zip(commands, inputs, actual, expected)):
        #     if command == 'search' and a != e:
        #         print(f'{command=} {i=} {a=} {e=}')
        self.assertEqual(actual, expected)

    def test2(self):
        commands = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
        inputs = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
        actual = self.run_with(commands, inputs)
        expected = [None, None, None, None, False, True, True, True]
        self.assertEqual(actual, expected)

    def run_with(self, commands: [str], inputs: [str]) -> [None | bool]:
        res = []
        s = WordDictionary()
        for command, input_value in list(zip(commands, inputs)):
            if command == 'WordDictionary':
                res.append(None)
            elif command == 'addWord':
                s.addWord(input_value[0])
                res.append(None)
            elif command == 'search':
                res.append(s.search(input_value[0]))
        return res
