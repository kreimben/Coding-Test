"""
https://www.algoexpert.io/questions/validate-bst
Validate BST
"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def check(tree: BST, p_min: int, p_max: int) -> bool:
    if tree.value < p_min or tree.value >= p_max:
        return False

    if tree.left is not None:
        if not check(tree.left, p_min=p_min, p_max=tree.value):
            return False

    if tree.right is not None:
        if not check(tree.right, p_min=tree.value, p_max=p_max):
            return False

    return True


def validateBst(tree: BST) -> bool:
    return check(tree, float('-INF'), float('INF'))


root = BST(10)
root.left = BST(5)
# root.left.left = BST(2)
# root.left.left.left = BST(1)
root.left.right = BST(10)
# root.left.right.right = BST(11)
root.right = BST(15)
# root.right.left = BST(5)
# root.right.left.right = BST(14)
# root.right.right = BST(22)

assert validateBst(root) == False
