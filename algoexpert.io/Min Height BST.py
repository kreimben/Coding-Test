"""
https://www.algoexpert.io/questions/min-height-bst
Min Height BST
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def minHeightBst(array: [int]):  # [1, 2, 5, 7, 10, 13, 14, 15, 22]
    def dfs(array: [int]) -> BST:
        mid_number = array[len(array) // 2]  # 10
        left = array[:len(array) // 2]
        right = array[len(array) // 2 + 1:]
        root = BST(mid_number)
        root.left = dfs(left) if left else None
        root.right = dfs(right) if right else None
        return root

    # Middle value of array should be root's value.
    return dfs(array)
