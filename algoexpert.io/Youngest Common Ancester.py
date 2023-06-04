"""
https://www.algoexpert.io/questions/youngest-common-ancestor
Youngest Common Ancester
"""


# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Brute force.
    # Find all ancestors.
    oa = []
    ta = []
    curr = descendantOne
    while curr:
        oa.append(curr)
        curr = curr.ancestor

    curr = descendantTwo
    while curr:
        ta.append(curr)
        curr = curr.ancestor

    # Let's compare with each
    # oa = [E, B, A]
    # ta = [I, D, B, A]
    # I should use stack.
    # Compare should starts from the end of array.
    # And there are not gonna be empty stack from scratch.
    prev = None
    while oa and ta:
        if oa[-1].name != ta[-1].name:
            # prev should be returned.
            return prev
        else:
            oa.pop()
            prev = ta.pop()


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class AncestralTree(AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"])
        trees["B"].addDescendants(trees["D"], trees["E"])
        trees["D"].addDescendants(trees["H"], trees["I"])
        trees["C"].addDescendants(trees["F"], trees["G"])

        yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
        self.assertTrue(yca == trees["B"])


t = TestProgram()
t.test_case_1()
