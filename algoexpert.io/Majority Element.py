"""
Majority Element
https://www.algoexpert.io/questions/majority-element
"""


def majorityElement(array):
    """
    O(n^3) time | O(1) space
    """
    for num in set(array):  # to remove duplicated number
        count = 0
        for number in array:
            if num == number:
                count += 1
            else:
                count -= 1
        if count >= 1:
            # that is majority number.
            return num
