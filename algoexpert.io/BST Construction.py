"""
https://www.algoexpert.io/questions/bst-construction
BST Construction
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
        return self

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def remove(self, value, pnode=None):
        curr = self
        while curr is not None:
            if value < curr.value:
                pnode = curr
                curr = curr.left
            elif curr.value < value:
                pnode = curr
                curr = curr.right
            else:
                if curr.left is not None and curr.right is not None:
                    curr.value = curr.right.getMinValue()
                    curr.right.remove(curr.value, curr)
                elif pnode is None:
                    if curr.left is not None:
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right is not None:
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else:
                        pass
                elif pnode.left == curr:
                    pnode.left = curr.left if curr.left is not None else curr.right
                elif pnode.right == curr:
                    pnode.right = curr.left if curr.left is not None else curr.right
                break
        return self

    def getMinValue(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

root.insert(12)
assert root.right.left.left.value == 12

root.remove(10)
assert (not root.contains(10)) == True
assert (root.value == 12) == True

assert (root.contains(15)) == True
