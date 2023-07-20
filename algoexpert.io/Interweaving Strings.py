"""
Interweaving Strings
https://www.algoexpert.io/questions/interweaving-strings
"""


def interweavingStrings(one, two, three):
    """
    algoexpert video solution
    """
    if len(three) != len(one) + len(two):
        return False

    def is_valid(i, j):
        if i + j == len(three):
            return True

        if i < len(one) and one[i] == three[i + j]:
            if is_valid(i + 1, j):
                return True

        if j < len(two) and two[j] == three[i + j]:
            if is_valid(i, j + 1):
                return True

        return False

    return is_valid(0, 0)


assert interweavingStrings("algo", "frog", "fralgogo") == True
# assert interweavingStrings("algoexpert", "your-dream-job", "ayloguore-xdpreeratm-job") == True
