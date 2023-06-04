"""
https://www.algoexpert.io/questions/one-edit
One Edit
"""


def oneEdit(stringOne, stringTwo):
    if abs(len(stringOne) - len(stringTwo)) > 1:
        return False
    elif len(stringOne) == len(stringTwo):
        count = 0
        for i in range(len(stringOne)):
            if stringOne[i] != stringTwo[i]:
                count += 1
        if count <= 1:
            return True
        else:
            return False
    else:  # difference of length of its string is only 1.
        for i in range(max(len(stringOne), len(stringTwo))):
            if i > len(stringOne) - 1:
                return True
            elif i > len(stringTwo) - 1:
                return True
            else:
                # If i in both strings range.
                if stringOne[i] != stringTwo[i]:
                    if len(stringOne) > len(stringTwo):
                        stringOne = stringOne[:i] + stringOne[i + 1:]
                    else:
                        stringTwo = stringTwo[:i] + stringTwo[i + 1:]
                    if stringOne == stringTwo:
                        return True
                    else:
                        return False


assert oneEdit('a', 'ab') == True
assert oneEdit('ab', 'b') == True
