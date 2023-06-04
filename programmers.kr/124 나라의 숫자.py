"""
https://school.programmers.co.kr/learn/courses/30/lessons/12899
124 나라의 숫자
"""


def solution(n):
    num = int(n)
    s = ['4', '1', '2']
    result = ''
    while num > 0:
        result += s[num % 3]
        if num % 3:
            num = num // 3
        else:
            num = (num // 3) - 1
    return result[::-1]


print(solution(1))
# assert solution(1) == 1  # 3 * 0 + 1 => 1
# assert solution(2) == 2  # 3 * 0 + 2 => 2
# assert solution(3) == 4  # 3 * 1 + 0 => 4
# assert solution(4) == 11  # 3 * 1 + 1 => 11
# assert solution(5) == 12  # 3 * 1 + 2 => 12
# assert solution(6) == 14  # 3 * 1 + 4 => 14
# assert solution(7) == 21  # 3 * 2 + 1 => 21
# assert solution(8) == 22  # 3 * 2 + 2 => 22
# assert solution(9) == 24  # 3 + 2 + 4 => 24
# assert solution(10) == 41  # 3 * 3 + 1 => 41
# assert solution(50) == 1212  # 27 * 1 + 9 * 2 + 3 * 1 + 2 = 1212
# assert solution(100) == 4141  # 27 * 3 + 9 * 2 + 3 * 0 + 1 => 4201
