"""
https://www.algoexpert.io/questions/multi-string-search
Multi String Search
"""


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
        return True


def multiStringSearch(bigString, smallStrings):
    b = SuffixTrie(bigString)
    results = []
    for block in smallStrings:
        if b.contains(block):
            results.append(True)
        else:
            results.append(False)
    return results


assert multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]) \
       == [True, False, True, True, False, True, False]
