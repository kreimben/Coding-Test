"""
https://leetcode.com/problems/copy-list-with-random-pointer/description/
Copy List with Random Pointer
"""
"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def index(self, node, target):
        index = 0
        curr = node
        while curr:
            if curr == target:
                return index
            else:
                index += 1
                curr = curr.next

    def get_node(self, node, index):
        if index is None:
            return None
        curr = node
        while index > 0:
            index -= 1
            curr = curr.next
        return curr

    def copyRandomList(self, head):
        # Extract current values in linked list.
        curr = head
        values = []
        randoms = []
        while curr:
            values.append(curr.val)
            randoms.append(curr.random)
            curr = curr.next
        # Just create new one without dealing with random.
        if len(values) == 0:
            return None

        root = Node(values.pop(0))
        curr = root
        while values:
            curr.next = Node(values.pop(0))
            curr = curr.next

        # And put indexed random nodes.
        for i, random in enumerate(randoms):
            target = self.get_node(root, i)
            random_index = self.index(head, random)
            target.random = self.get_node(root, random_index)

        return root
