"""
https://school.programmers.co.kr/learn/courses/30/lessons/131127
할인 행사
"""


def solution(want: [str], number: [int], discount: [str]) -> int:
    days = 0
    dic = {}

    # 첫번째로, dict 작업을 해준다.
    for i in range(len(want)):
        dic[want[i]] = number[i]

    del i

    # 이제 n번째 날짜 부터 열흘간 조건에 맞는지 살펴 보면 된다.
    for i in range(len(discount) - 9):
        seek = discount[i:i + 10]

        # 계속해서 열흘간 비교해야하니 dic을 그대로 복사해서 비교한다.
        t = dic.copy()  # deep copy
        for j, item in enumerate(seek):
            if item in t:
                t[item] -= 1

        left = False
        for value in t.values():
            if value > 0:
                left = True  # 남은게(세일 하지 않은 것이) 있는지 검사
                break

        if left:
            continue
        else:
            days += 1

    return days


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                "banana", "apple", "banana"]))
print(solution(["apple"], [10],
               ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
