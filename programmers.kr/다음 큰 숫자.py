"""
https://school.programmers.co.kr/learn/courses/30/lessons/12911
다음 큰 숫자
"""

def solution(n: int):
    n_one_count = 0



# def solution(n: int):
#     n_base = str(bin(n))[2:]
#     one_count_n = one_count(n_base)
#
#     n_next = n + 1
#
#     while True:
#         n_next_base = str(bin(n_next))[2:]
#
#         one_count_n_next = one_count(n_next_base)
#
#         if one_count_n == one_count_n_next:
#             return n_next
#
#
# def one_count(n: str) -> int:
#     count = 0
#     for cha in n:
#         if cha == '1':
#             count += 1
#
#     return count


assert solution(78) == 83
assert solution(15) == 23
