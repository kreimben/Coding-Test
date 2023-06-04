"""
https://school.programmers.co.kr/learn/courses/30/lessons/12973?language=python3
짝지어 제거하기
"""

"""
정확성: 60.2
효율성: 0.0
합계: 60.2 / 100.0
"""

def solution(s: str):
    stack = []
    text = s

    while text:
        if not len(stack):
            stack.append(text[0])
        elif stack[len(stack) - 1] == text[0]:
            stack.pop()
        elif stack[len(stack) - 1] != text[0]:
            stack.append(text[0])

        text = text[1:]

    if not stack and not len(text):
    # if not stack and text_index == len(text) - 1:
        return 1
    else:
        return 0


# print(solution(''))
print(solution('aaaaa'))
print(solution('baabaa'))
print(solution('cdcd'))
