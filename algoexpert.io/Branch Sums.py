"""
https://www.algoexpert.io/questions/branch-sums
Branch Sums
"""


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(tree: BinaryTree, given_value: int, results: [int]):
    """
    :param tree: Binary Tree
    :return: Sum of its' children value.
    """
    if tree is None:
        return
    g = given_value + tree.value
    if tree.right is None and tree.left is None:
        results.append(g)
        return
    dfs(tree.left, g, results)
    dfs(tree.right, g, results)


def branchSums(root):
    """
    전형적인 DFS문제이다.
    """
    results = []
    dfs(root, 0, results)
    return results


one = BinaryTree(1)

two = BinaryTree(2)
three = BinaryTree(3)
one.left = two
one.right = three

four = BinaryTree(4)
five = BinaryTree(5)
two.left = four
two.right = five

six = BinaryTree(6)
seven = BinaryTree(7)
three.left = six
three.right = seven

eight = BinaryTree(8)
nine = BinaryTree(9)
four.left = eight
four.right = nine

ten = BinaryTree(10)
five.left = ten

assert branchSums(one) == [15, 16, 18, 10, 11]
