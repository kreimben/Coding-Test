"""
https://www.algoexpert.io/questions/validate-subsequence
Validate Subsequence
"""


def isValidSubsequence(array: [int], sequence: [int]):
    """
    아래 코드 보다 조금 더 깔끔한 버전
    """
    for i, num in enumerate(array):
        target = sequence[0]
        if target == num:
            sequence.pop(0)
            if not sequence:
                break

    if len(sequence) != 0:
        return False

    return True


# def isValidSubsequence(array: [int], sequence: [int]):
#     """
#     Try Except문을 썼지만 이게 맞는건지는 모르겠다.
#     아무튼 내가 쓴 식대로라면, 이렇게 하는것이 최선이다.
#     """
#     last = -1  # last popped index of array.
#     while sequence:
#         target = sequence.pop(0)
#         try:
#             if target not in array or last > array.index(target, last + 1):
#                 return False
#         except ValueError:
#             return False
#         last = array.index(target, last + 1)
#
#     if len(array) == 0 and len(sequence) == 0:
#         return False
#     else:
#         return True


assert isValidSubsequence([1, 1, 6, 1], [1, 1, 1, 6]) == False
assert isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 5]) == False
