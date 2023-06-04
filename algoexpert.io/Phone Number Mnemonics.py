"""
https://www.algoexpert.io/questions/phone-number-mnemonics
Phone Number Mnemonics
"""


def phoneNumberMnemonics(phoneNumber):
    d = {
        '1': ['1'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': ['0'],
    }

    # Calculate every combination.
    stack = []
    for ch in phoneNumber:
        stack.append(
            d[ch]
        )

    from itertools import product
    result = [''.join(line) for line in list(product(*stack))]
    return result


assert phoneNumberMnemonics("1905") == ["1w0j", "1w0k", "1w0l", "1x0j",
                                        "1x0k", "1x0l", "1y0j", "1y0k",
                                        "1y0l", "1z0j", "1z0k", "1z0l"]
