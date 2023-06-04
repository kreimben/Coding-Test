"""
https://www.algoexpert.io/questions/suffix-trie-construction
Suffix Trie Construction
"""


# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            block = string[i:]
            curr = self.root
            for index, ch in enumerate(block):
                if curr.get(ch):
                    curr = curr[ch]
                else:
                    curr[ch] = {}  # Put just empty dict for reference.
                    curr = curr[ch]
            else:
                curr.update({self.endSymbol: True})

    def contains(self, string):
        curr = self.root
        for i, ch in enumerate(string):
            if not curr.get(ch):
                return False
            curr = curr[ch]
        else:
            if curr.get(self.endSymbol) == True:
                return True
            else:
                return False


s = SuffixTrie('babc')
assert s.root == {
    "c": {"*": True},
    "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
    "a": {"b": {"c": {"*": True}}},
}
assert s.contains('abc') == True
