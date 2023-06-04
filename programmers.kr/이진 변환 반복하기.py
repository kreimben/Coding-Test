"""
https://school.programmers.co.kr/learn/courses/30/lessons/70129
이진 변환 반복하기
"""


def solution(s: str):
    convert_num = 1
    zero_count = 0

    while True:
        one_count = 0
        for char in s:
            if char == '1':
                one_count += 1
            elif char == '0':
                zero_count += 1

        s = str(bin(one_count))[2:]

        if s == '1':
            break

        convert_num += 1

    return [convert_num, zero_count]


print(solution('110010101001'))
print(solution('01110'))
print(solution('1111111'))
