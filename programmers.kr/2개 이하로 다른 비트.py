"""
https://school.programmers.co.kr/learn/courses/30/lessons/77885#
2개 이하로 다른 비트
"""


def solution(numbers: [int]):
    results = []
    for num in numbers:
        b = bin(num)
        b = b[2:]

        if num % 2 == 0:
            # 어차피 짝수를 2진법으로 나타내면 xxxxx0의 형태가 된다.
            # 따라서 맨 끝자리에 1을 더해주면 됨으로 짝수의 경우 그냥 1을 더해주면 된다.
            results.append(num + 1)
        else:
            # 홀수의 경우 0이 나오는 가장 낮은 자리를 1로 높여주고
            # 그 뒤를 0으로 만들어 주면 가장 작은 차이로 가장 작은 수가 나온다.
            last_zero_index = 0
            temp = []
            for i, n in enumerate(b):
                temp.append(n)
                if n == '0':
                    last_zero_index = i

            if last_zero_index == 0:
                # 만약 제일 나중에 오는 0의 위치가 0이라면 해당 숫자에 0이 없는 것이니
                # 맨 앞에 1을 넣어주고 그 다음 숫자를 0으로 만들면 된다.
                temp.insert(0, '1')
                temp[1] = '0'
            else:
                temp[last_zero_index] = '1'
                if len(temp) - 1 > last_zero_index:
                    temp[last_zero_index + 1] = '0'

            results.append(
                int("".join(temp), 2)
            )
    return results


assert (solution([2, 7]) == [3, 11])

f = [1001, 337, 0, 1, 333, 673, 343, 221, 898, 997, 121, 1015, 665, 779, 891, 421, 222, 256, 512, 128, 100]
s = [1002, 338, 1, 2, 334, 674, 347, 222, 899, 998, 122, 1019, 666, 781, 893, 422, 223, 257, 513, 129, 101]
assert (solution(f) == s)
