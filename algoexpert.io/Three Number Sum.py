"""
https://www.algoexpert.io/questions/three-number-sum
Three Number Sum
"""


def threeNumberSum(array: [int], targetSum: int):
    array.sort()
    results = []

    for i in range(len(array)):
        current = i
        left = i + 1
        right = len(array) - 1
        while left != right and left < right:
            current_sum = array[current] + array[left] + array[right]

            if current_sum > targetSum:
                right -= 1
            elif current_sum < targetSum:
                left += 1
            else:  # current == targetSum
                result = [array[current], array[left], array[right]]
                left += 1
                right -= 1
                results.append(result)
    return results


assert threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
