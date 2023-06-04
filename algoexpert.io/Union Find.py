"""
https://www.algoexpert.io/questions/union-find
Union Find
"""


class UnionFind:
    parents: dict

    def __init__(self):
        self.parents = {}

    def createSet(self, value):
        self.parents[value] = value

    def find(self, value):
        if value not in self.parents:
            return None
        curr = value
        while curr != self.parents[curr]:
            curr = self.parents[curr]
        return curr

    def union(self, valueOne, valueTwo):
        # Insert sets of valueTwo to head of valueOne.
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        headOne = self.find(valueOne)
        headTwo = self.find(valueTwo)

        self.parents[headTwo] = headOne


u = UnionFind()
u.createSet(10)
u.createSet(5)
assert u.find(10) == 10
u.union(10, 5)
