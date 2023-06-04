"""
https://www.algoexpert.io/questions/merge-binary-trees
Merge Binary Trees
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


def mergeBinaryTrees(tree1, tree2):
    def merge(root, tree1, tree2):
        if tree1 and tree2:
            # Merge the node each other.
            root = BinaryTree(tree1.value + tree2.value)

            root.left = merge(root.left, tree1.left, tree2.left)
            root.right = merge(root.right, tree1.right, tree2.right)

        elif tree1 and not tree2:
            root = BinaryTree(tree1.value)

            root.left = merge(root.left, tree1.left, None)
            root.right = merge(root.right, tree1.right, None)

        elif tree2 and not tree1:
            root = BinaryTree(tree2.value)

            root.left = merge(root.left, None, tree2.left)
            root.right = merge(root.right, None, tree2.right)

        return root

    return merge(BinaryTree(0), tree1, tree2)


tree1 = BinaryTree(1)
tree1.left = BinaryTree(3)
tree1.left.left = BinaryTree(7)
tree1.left.right = BinaryTree(4)
tree1.right = BinaryTree(2)

tree2 = BinaryTree(1)
tree2.left = BinaryTree(5)
tree2.left.left = BinaryTree(2)
tree2.right = BinaryTree(9)
tree2.right.left = BinaryTree(7)
tree2.right.right = BinaryTree(6)

actual = mergeBinaryTrees(tree1, tree2)
assert actual.value == 2
assert actual.left.value == 8
assert actual.left.left.value == 9
assert actual.left.right.value == 4
assert actual.right.value == 11
assert actual.right.left.value == 7
assert actual.right.right.value == 6
