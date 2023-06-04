"""
https://www.algoexpert.io/questions/bst-traversal
BST Traversal
"""


def inOrderTraverse(tree, array):
    if tree is None:
        return
    # Left
    inOrderTraverse(tree.left, array)
    # Visit // Save visited values to array.
    array.append(tree.value)
    # Right
    inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is None:
        return
    # Visit
    array.append(tree.value)
    # Left
    preOrderTraverse(tree.left, array)
    # Right
    preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is None:
        return
    # Left
    postOrderTraverse(tree.left, array)
    # Right
    postOrderTraverse(tree.right, array)
    # Visit
    array.append(tree.value)
    return array
