"""
https://school.programmers.co.kr/learn/courses/30/lessons/17687
n진수 게임
"""


def n_number(x: int, r: int) -> str:
    """정수값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
    if not x:
        return '0'

    d = ''  # 변환 후의 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]  # 해당하는 문자를 꺼내 결합, 나머지를 나열하기 위함
        x //= r

    return d[::-1]


def solution(n: int, t: int, m: int, p: int):
    """
    n = 16진수를 쓰면서
    t = 16개의 숫자를 자신의 순서에 맞게 구하려한다.
    m = 2명의 플레이어가 있을때
    p = 1번째 순서이다.
    """
    results = ''
    order = 1
    left_to_speak = []
    while len(results) < t:
        b = n_number(order - 1, n)

        left_to_speak += b

        if order % m == abs(p - m):
            # 자신의 차례
            results += left_to_speak.pop(0)
        else:
            left_to_speak.pop(0)

        order += 1
    return results


assert (solution(2, 4, 2, 1) == "0111")
assert (solution(16, 16, 2, 1) == "02468ACE11111111")
assert (solution(16, 16, 2, 2) == "13579BDF01234567")
