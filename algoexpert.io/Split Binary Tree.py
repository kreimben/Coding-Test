"""
https://www.algoexpert.io/questions/split-binary-tree
Split Binary Tree
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree(tree):
    total = 0

    # hint 1
    def traverse(node):
        nonlocal total
        if node is None:
            return
        total += node.value
        traverse(node.left)
        traverse(node.right)

    traverse(tree)  # calculate total sum of binary tree.
    should_continue = True

    def count(node):
        nonlocal should_continue, total
        if node is None:
            return
        # hint 4 => post-order traversal
        l = count(node.left)
        r = count(node.right)

        if (l and l == total / 2) or (r and r == total / 2):
            should_continue = False

        ret = node.value
        if l:
            ret += l
        if r:
            ret += r
        return ret

    count(tree)

    if not should_continue:
        return total / 2
    else:
        return 0
