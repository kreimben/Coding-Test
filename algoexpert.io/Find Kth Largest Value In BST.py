"""
https://www.algoexpert.io/questions/find-kth-largest-value-in-bst
Find Kth Largest Value In BST
"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree: BST, k: int):
    result = []

    def dfs(tree: BST):
        # Right
        if tree.right is not None:
            r = dfs(tree.right)
            if r is not None:
                return r
        # Visit
        result.append(tree.value)

        if len(result) > k - 1:
            return result[k - 1]
        # Left
        if tree.left is not None:
            r = dfs(tree.left)
            if r is not None:
                return r

    return dfs(tree)


root = BST(15)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.left.right = BST(3)
root.left.right = BST(5)
root.right = BST(20)
root.right.left = BST(17)
root.right.right = BST(22)
k = 6
expected = 5
actual = findKthLargestValueInBst(root, k)
assert actual == expected
