"""
https://www.algoexpert.io/questions/valid-ip-addresses
Valid IP Addresses
"""


def validIPAddresses(string):
    def checkValid(string):
        s = string.split('.')
        for n in s:
            f = len(n) > 3
            ss = len(n) > 1 and n[0] == '0'
            t = not (0 <= int(n) < 2 ** 8)

            if f or ss or t:
                return False
        return True

    # Just input . in each of index.
    ips = []

    def insert(indices, string):
        # Index cannot be duplicated.
        if len(indices) == 3:
            ips.append(
                string[:indices[0]] + '.' +
                string[indices[0]:indices[1]] + '.' +
                string[indices[1]:indices[2]] + '.' +
                string[indices[2]:]
            )

        # find new available index.
        for i in range(indices[-1] + 1, len(string)):
            insert(indices + [i], string)

    for i in range(1, 4):
        insert([i], string)
    results = []
    for ip in ips:
        if checkValid(ip):
            results.append(ip)

    return results


assert validIPAddresses("3700100") == ["3.70.0.100", "37.0.0.100"]
assert validIPAddresses("1921680") == ["1.9.216.80", "1.92.16.80", "1.92.168.0", "19.2.16.80", "19.2.168.0",
                                       "19.21.6.80", "19.21.68.0", "19.216.8.0", "192.1.6.80", "192.1.68.0",
                                       "192.16.8.0"]
