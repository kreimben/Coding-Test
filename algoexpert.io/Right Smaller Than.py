"""
https://www.algoexpert.io/questions/right-smaller-than
Right Smaller Than
"""


def rightSmallerThan(array):
    s = []
    for i, num in enumerate(array):
        s.append((i, num))
    results = [0] * len(array)
    for index, number in s:
        count = 0
        for target_index in range(index + 1, len(s)):
            target = s[target_index][1]
            if number > target:
                count += 1
        else:
            results[index] = count
    return results


assert rightSmallerThan([8, 5, 11, -1, 3, 4, 2]) == [5, 4, 4, 0, 1, 1, 0]
