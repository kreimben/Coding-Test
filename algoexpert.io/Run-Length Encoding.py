"""

Run-Length Encoding
"""


def runLengthEncoding(string):
    result = ''
    train = ''  # string which only stores same character.
    for ch in string:
        if train:
            if train[-1] == ch:
                if 0 <= len(train) < 9:
                    train += ch
                    continue
                else:  # only if train's length is over 9
                    result += f'{len(train)}{ch}'
            else:
                # Make train empty.
                result += f'{len(train)}{train[0]}'
        train = ch
    else:
        # Make train empty.
        result += f'{len(train)}{train[-1]}'
        train = ''

    return result


assert runLengthEncoding("AAAAAAAAAAAAABBCCCCDD") == '9A4A2B4C2D'
