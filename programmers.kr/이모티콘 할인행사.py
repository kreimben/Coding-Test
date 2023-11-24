"""
이모티콘 할인행사
https://school.programmers.co.kr/learn/courses/30/lessons/150368
"""


def solution(users: [[int]], emoticons: [int]):
    off = [10, 20, 30, 40]
    res = []  # (pass_count, sales_amount)

    sales = []
    res = []

    def dfs():
        nonlocal sales, res
        if len(sales) >= len(emoticons):
            pass_count = 0  # 이모티콘 플러스 가입자 수
            temp = [0] * len(users)

            for j in range(len(users)):
                for i, rate in enumerate(sales):
                    if rate >= users[j][0]:
                        temp[j] += emoticons[i] - emoticons[i] * rate * 0.01

            total_amount = 0
            for i, val in enumerate(temp):
                if val >= users[i][1]:
                    pass_count += 1
                    temp[i] = 0
                else:
                    total_amount += temp[i]

            res.append((pass_count, total_amount))  # calculate
            return
        for rate in off:
            sales.append(rate)
            dfs()
            sales.pop()

    dfs()
    res.sort(key=lambda x: (x[0], x[1]))
    return res[-1]


assert solution([[40, 10000], [25, 10000]], [7000, 9000]) == [1, 5400]
