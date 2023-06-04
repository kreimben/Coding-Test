"""
https://www.algoexpert.io/questions/find-closest-value-in-bst
Find Closest Value
"""


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


"""
The solution must return closest value!!!
"""


def dfs(tree: BST, target: int, result: [int]):
    if tree is not None:
        a = abs(tree.value - target)
        if a < abs(result[0] - target):
            result[0] = tree.value

        if tree.value > target and tree.left is not None:
            dfs(tree.left, target, result)
        elif tree.value <= target and tree.right is not None:
            dfs(tree.right, target, result)


def findClosestValueInBst(tree: BST, target: int):
    result = [float('INF')]
    dfs(tree, target, result)
    return result[0]


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
assert findClosestValueInBst(root, 12) == 13

root = BST(100)
root.left = BST(5)
root.right = BST(502)
root.left.left = BST(2)
root.left.right = BST(15)
root.right.left = BST(204)
root.right.right = BST(55000)
root.left.left.left = BST(1)
root.left.left.right = BST(3)
root.left.right.left = BST(5)
root.left.right.right = BST(22)
root.left.left.left.left = BST(-51)
root.left.left.left.right = BST(1)
root.left.left.left.left.left = BST(-403)
assert findClosestValueInBst(root, 100) == 100
assert findClosestValueInBst(root, -70) == -51
