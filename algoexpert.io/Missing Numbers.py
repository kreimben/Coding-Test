"""
https://www.algoexpert.io/questions/missingNumbers
Missing Numbers
"""


def missingNumbers(nums):
    res = []
    sample = [i for i in range(1, len(nums) + 3)]

    for num in sample:
        if num not in nums:
            res.append(num)

    return res

# def missingNumbers(nums: [int]) -> [int]:
#     res = set([i for i in range(1, len(nums) + 3)])
#     res = res.difference(nums)
#     return sorted(res)
