"""
https://school.programmers.co.kr/learn/courses/30/lessons/12913?language=python3
땅따먹기
"""


# https://school.programmers.co.kr/questions/34333
def solution(land):
    answer = 0
    for i in range(1, len(land)):
        for j in range(4):
            tmp = land[i - 1][j]
            land[i - 1][j] = -1
            land[i][j] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2], land[i - 1][3])
            land[i - 1][j] = tmp
    answer = max(land[i][0], land[i][1], land[i][2], land[i][3])
    return answer


# def solution(land: [[int]]):
#     result = 0
#     prev_max_col_index = -1
#
#     for row_index in range(len(land)):
#         this_row = land[row_index]
#         max_col_index_in_this_row = 0
#
#         for col_index in range(4):
#             if this_row[col_index] > this_row[max_col_index_in_this_row]:
#                 if prev_max_col_index == col_index:
#                     continue
#                 max_col_index_in_this_row = col_index
#
#         result += this_row[max_col_index_in_this_row]
#         prev_max_col_index = max_col_index_in_this_row
#
#     return result


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
