"""
https://school.programmers.co.kr/learn/courses/30/lessons/132265
롤케이크 자르기
"""
from collections import Counter


# def count_without_duplicates(arr: [int]) -> int:
#     return len(list(set(arr)))
#
#
# def solution(topping: [int]) -> int:
#     # 우선 2개로만 자르면 된다.
#     # 비교는 그 뒤에 해도 되니
#     # 우선 index에 따라 2조각을 내버린 후
#     # 종류의 갯수가 같은 경우의 수를
#     # 구해주면 된다.
#     first = topping[:1]
#     second = topping[1:]
#     # for문으로 돌지 않고 이렇게 수동으로 하는 이유는
#     # 그렇게 냈다간 무조건 시간 제한에 걸리기 때문이다.
#     # Python String Slicing은 정말로 편리하지만
#     # 존나게 느리다.
#     count = 0
#     while len(second) > 2:
#         f = count_without_duplicates(first)
#         s = count_without_duplicates(second)
#         if f == s:
#             count += 1
#         # second에 있는 맨 앞 element를
#         # first 맨뒤에 넣어준다.
#         # 사실 Python String Slicing의 수동 버전이다.
#         first.append(
#             second.pop(0)
#         )
#     return count

# 위에는 내가 푼 기본적인 접근 법이고,
# 저렇게 해도 String Slicing과 별로 속도가 다르지 않아
# 빠른 정답을 가져와 여기에 적었다.
def solution(topping):
    answer = 0
    total = Counter(topping)
    set1 = set()
    while len(topping) > 1:
        element = topping.pop()
        set1.add(element)
        if total[element] > 1:
            total[element] = total[element] - 1
        else:
            del total[element]

        if len(total) == len(set1):
            answer += 1
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))  # 2
print(solution([1, 2, 3, 1, 4]))  # 0
