"""
https://school.programmers.co.kr/learn/courses/30/lessons/12981?language=python3
영어 끝말잇기
"""


def solution(n, words):
    told = []

    for index, word in enumerate(words):
        if word in told:
            results = [index % n + 1, index // n + 1]
            return results
        elif told and told[-1][-1] != word[0]:
            results = [index % n + 1, index // n + 1]
            return results

        told.append(word)

    return [0, 0]


assert solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]) == [3, 3]
assert solution(5,
                ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish",
                 "hang", "gather", "refer", "reference", "estimate", "executive"]) == [0, 0]
assert solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]) == [1, 3]
