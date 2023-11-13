"""
개인정보 수집 유효기간
2023 KAKAO BLIND RECRUITMENT
유형 = Brute-Force
https://school.programmers.co.kr/learn/courses/30/lessons/150370
"""


def convert_day_to_number(day_string: str) -> int:
    # 28 days in a month,
    # 12 months in a year
    # So we can substitute as a days.
    MONTH = 28  # days
    YEAR = 12 * MONTH  # days
    s = day_string.split('.')
    y = (int(s[0]) - 2000) * YEAR
    m = int(s[1]) * MONTH
    d = int(s[2].split()[0])
    return y + m + d


def solution(today, terms, privacies):
    TODAY = convert_day_to_number(today)

    t = {}
    for term in terms:
        t[term.split()[0]] = term.split()[1]

    res = []

    for index, privacy in enumerate(privacies):
        day, grade = privacy.split()
        DAY = convert_day_to_number(day)
        DUE = DAY + int(t[grade]) * 28
        if TODAY >= DUE:
            res.append(index + 1)

    return res
