"""
https://www.algoexpert.io/questions/reverse-words-in-string
Reverse Words In String
"""


def reverseWordsInString(string):
    # We can separate between words with whitespace.

    # First, Reverse ALL CHARACTERS.
    result = ''
    for ch in reversed(string):
        result += ch
    # Second, Reverse ALL WORDS.
    prev = 0  # We start from zero index and need previous index.
    for i in range(len(result) + 1):
        if i == len(result):
            # End of string
            result = result[:prev] + result[prev:i][::-1]
        elif result[i] == ' ' and i != 0:
            result = result[:prev] + result[prev:i][::-1] + result[i:]
            prev = i + 1

    return result


reverseWordsInString("AlgoExpert is the best!")
