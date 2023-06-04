"""
https://school.programmers.co.kr/learn/courses/30/lessons/42883
큰 수 만들기
"""


def slice_ith_element(s: str, i: int) -> str:
    result = ''

    for index in range(len(s)):
        if i != index:
            result += s[index]

    return result


def check(s: str, target_number: int, maximum: [int]):
    if len(s) != target_number:
        for i in range(len(s)):
            check(slice_ith_element(s, i), target_number, maximum)
    else:
        if int(s) > max(maximum):
            maximum.append(int(s))


def solution(number: str, k: int) -> str:
    maximum = [0]
    check(number, len(number) - k, maximum)
    return str(max(maximum))


assert solution("654321", 1) == '65432'
assert solution("654321", 5) == "6"
assert solution("4177255555", 4) == "775555"
assert solution("4321", 1) == "432"
assert solution("4177252841", 4) == "775841"
assert solution("1231234", 3) == "3234"
assert solution("1924", 2) == "94"
