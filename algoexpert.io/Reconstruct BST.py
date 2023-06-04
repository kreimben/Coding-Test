"""
https://www.algoexpert.io/questions/reconstruct-bst
Reconstruct BST
"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value}'

    def __str__(self):
        return f'{self.value}'


def reconstructBst(preOrderTraversalValues: [int]):
    value = preOrderTraversalValues.pop(0)
    root = BST(value)
    # Split array until len(array) == 0
    left, right = [], []
    left_closed = False
    for num in preOrderTraversalValues:
        if not left_closed:
            if root.value > num:
                left.append(num)
            else:
                left_closed = True
                right.append(num)
        else:
            right.append(num)

    root.left = reconstructBst(left) if left else None
    root.right = reconstructBst(right) if right else None

    return root


reconstructBst([10, 4, 2, 1, 3, 5, 5, 6, 5, 5, 9, 7, 17, 19, 18, 18, 19])
reconstructBst([5, 6, 7, 8])
reconstructBst([10, 9, 8, 7, 6, 5])
reconstructBst([10, 4, 2, 1, 5, 17, 19, 18])
