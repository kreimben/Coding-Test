"""
https://www.algoexpert.io/questions/generate-document
Generate Document
"""


def pop_string(s: str):
    results = s[-1]
    return s[:-1], results


def generateDocument(characters, document):
    d = {}
    while characters:
        characters, char = pop_string(characters)
        if d.get(char):
            d[char] += 1
        else:
            d[char] = 1

    while document:
        document, char = pop_string(document)
        if d.get(char):
            d[char] -= 1
        else:
            return False

    return True


assert generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!") == True
