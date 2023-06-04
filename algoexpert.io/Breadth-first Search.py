"""
https://www.algoexpert.io/questions/breadth-first-search
Breadth-first Search
"""
from collections import deque


class Node:
    q = deque()

    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        if self.name in array:
            return  # skip the visited node.

        for child in self.children:
            Node.q.append(child)

        array.append(self.name)

        # And visit child's nodes.
        # for child in self.q:
        while Node.q:
            child = Node.q.popleft()
            child.breadthFirstSearch(array)

        return array


graph = Node('A')
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")

assert graph.breadthFirstSearch([]) == ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
