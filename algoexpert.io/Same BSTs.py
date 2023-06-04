"""
https://www.algoexpert.io/questions/same-bsts
Same BSTs
"""


def sameBsts(arrayOne, arrayTwo):
    # First condition is length of two arrays and difference of root element.
    if len(arrayOne) != len(arrayTwo) or arrayOne[0] != arrayTwo[0]:
        return False

    # Second condition is difference of sorted two array.
    if sorted(arrayOne) != sorted(arrayTwo):
        return False

    # Last condition is to compare manually.
    # BST can be different by array's order.
    def make_bst(array):
        if not array:  # if array is empty
            return []

        root = array.pop(0)
        left = []
        right = []

        for val in array:
            if root > val:
                left.append(val)
            else:
                right.append(val)

        return [root] + make_bst(left) + make_bst(right)

    one = make_bst(arrayOne)
    two = make_bst(arrayTwo)

    if one != two:
        return False
    else:
        return True


assert sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 10], [10, 8, 5, 15, 2, 10, 12, 94, 81]) == False
