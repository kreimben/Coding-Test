"""
https://leetcode.com/problems/implement-trie-prefix-tree/description/
Implement Trie (Prefix Tree)
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            o = ord(ch) - ord('a')
            if curr.children[o] is None:
                curr.children[o] = TrieNode()
            curr = curr.children[o]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            o = ord(ch) - ord('a')
            if curr.children[o] is None:
                return False
            curr = curr.children[o]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            o = ord(ch) - ord('a')
            if curr.children[o] is None:
                return False
            curr = curr.children[o]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Trie:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        curr = self.d
        for ch in word:
            if not curr.get(ch, None):
                curr[ch] = {}
            curr = curr[ch]
        curr.update({'*': True})
        return

    def search(self, word: str) -> bool:
        curr = self.d
        for ch in word:
            if not curr.get(ch, None):
                return False
            curr = curr[ch]
        return curr.get('*', None)

    def startsWith(self, prefix: str) -> bool:
        curr = self.d
        for ch in prefix:
            if not curr.get(ch, None):
                return False
            curr = curr[ch]
        return True

# s = Trie()
# s.insert('apple')
# assert s.search('apple') == True
