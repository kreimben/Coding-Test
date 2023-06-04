"""
https://www.algoexpert.io/questions/palindrome-check
Palindrome Check
"""


def isPalindrome(net: str) -> bool:
    for i in range(len(net) // 2):
        n = net[i]
        r = net[len(net) - 1 - i]
        if net[i] != net[len(net) - 1 - i]:
            return False

    return True


# assert isPalindrome("abcdcba") == True
assert isPalindrome("a") == True
