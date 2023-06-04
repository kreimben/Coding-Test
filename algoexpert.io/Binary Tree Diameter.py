"""
https://www.algoexpert.io/questions/binary-tree-diameter
Binary Tree Diameter
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


# def count(results: [BinaryTree], chain: [BinaryTree], child: BinaryTree):
#     if child.left is None and child.right is None:
#         return results.append(chain)
#
#     if child.left:
#         count(results, chain + [child.left], child.left)
#     if child.right:
#         count(results, chain + [child.right], child.right)
#
#
# def binaryTreeDiameter(tree):
#     results = []
#     count(results, [tree], tree)
#     result = 0
#     # No need to sort cuz it naturally sorted.
#     if len(results) == 1:
#         return len(results[0])
#
#     for left in range(len(results)):
#         right = len(results) - 1
#         while left < right:
#             diff_index = 0
#             for i in range(min(len(results[left]), len(results[right]))):
#                 if results[left][i] != results[right][i]:
#                     diff_index = i
#                     break
#
#             temp = len(results[left][diff_index:]) + len(results[right][diff_index:])
#             result = max(result, temp)
#             right -= 1
#
#     return result


def count(tree):
    if tree is None:
        return (0, 0)

    left = count(tree.left)
    right = count(tree.right)

    return max(left[0], right[0], left[1] + right[1]), max(left[1], right[1]) + 1


def binaryTreeDiameter(tree):
    return count(tree)[0]


root = BinaryTree(1)
root.left = BinaryTree(3)
root.left.left = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)
root.left.right = BinaryTree(4)
root.left.right.right = BinaryTree(5)
root.left.right.right.right = BinaryTree(6)
root.right = BinaryTree(2)
expected = 6
actual = binaryTreeDiameter(root)
assert actual == expected
