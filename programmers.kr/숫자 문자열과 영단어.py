"""
https://school.programmers.co.kr/learn/courses/30/lessons/81301
숫자 문자열과 영단어
"""


def solution(s):
    result = ''
    while s:
        cha = s[0]
        if cha == 'z':
            result += '0'
            s = s[4:]
        elif cha == 'o':
            result += '1'
            s = s[3:]
        elif cha == 't':
            if s[:3] == 'two':
                result += '2'
                s = s[3:]
            else:
                result += '3'
                s = s[5:]
        elif cha == 'f':
            if s[:4] == 'four':
                result += '4'
            else:
                result += '5'
            s = s[4:]
        elif cha == 's':
            if s[:3] == 'six':
                result += '6'
                s = s[3:]
            else:
                result += '7'
                s = s[5:]
        elif cha == 'e':
            result += '8'
            s = s[5:]
        elif cha == 'n':
            result += '9'
            s = s[4:]
        else:
            result += cha
            s = s[1:]

    return int(result)


print(solution("one4seveneight"))
assert solution("one4seveneight") == 1478
assert solution("23four5six7") == 234567
assert solution("2three45sixseven") == 234567
assert solution("123") == 123
