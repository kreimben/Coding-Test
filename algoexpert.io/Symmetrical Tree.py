"""
https://www.algoexpert.io/questions/symmetrical-tree
Symmetrical Tree
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'


def symmetricalTree(tree):
    def get(tree):
        results = []
        if tree is None:
            return [tree]
        # Left
        results += get(tree.left)
        # Visit
        results.append(tree.value)
        # Right
        results += get(tree.right)

        return results

    left = get(tree.left)
    right = get(tree.right)
    if left == right[::-1]:
        return True
    else:
        return False


tree = BinaryTree(10)
tree.left = BinaryTree(5)
tree.right = BinaryTree(5)
tree.left.left = BinaryTree(7)
tree.left.right = BinaryTree(9)
tree.right.left = BinaryTree(9)
tree.right.right = BinaryTree(7)
expected = True
actual = symmetricalTree(tree)
assert actual == expected
