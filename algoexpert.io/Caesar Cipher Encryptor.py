"""
https://www.algoexpert.io/questions/caesar-cipher-encryptor
Caesar Cipher Encryptor
"""


def caesarCipherEncryptor(string: str, key: int):
    alphabet_len = ord('z') - ord('a') + 1
    key = key % alphabet_len

    new = ''
    if key != 0:
        for ch in string:
            aord = ord('a')
            zord = ord('z')

            new_ord = (ord(ch) + key)
            if new_ord > zord:
                new_ord -= zord
                new_ord += aord - 1
            elif aord > new_ord:
                new_ord += aord

            new += chr(new_ord)

        return new
    else:
        return string


assert caesarCipherEncryptor("ovmqkwtujqmfkao", 52) == 'ovmqkwtujqmfkao'
assert caesarCipherEncryptor('xyz', 2) == 'zab'
