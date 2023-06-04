"""
https://www.algoexpert.io/questions/zero-sum-subarray
Zero Sum Subarray
"""


def zeroSumSubarray(nums):
    result = False

    def check(amount: int):
        for start in range(len(nums) + 1 - amount):
            if sum(nums[start:start + amount]) == 0:
                return True
        return False

    for amount in range(len(nums), 0, -1):
        result = check(amount)
        if result:
            return result

    return result


assert zeroSumSubarray([1]) == False
assert zeroSumSubarray([0]) == True
