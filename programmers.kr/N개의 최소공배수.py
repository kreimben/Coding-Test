"""
https://school.programmers.co.kr/learn/courses/30/lessons/12953
N개의 최소공배수
"""


def get_dividends_nums(n: int) -> [int]:
    results = []

    d = 2
    while n != 1:
        if n % d != 0:
            d += 1
        else:
            n //= d
            results.append(d)

    results = set(results)

    return results


def solution(arr: [int]):
    arr.sort()
    bucket = []

    for n in arr:
        bucket += get_dividends_nums(n)

    bucket = set(bucket)

    results = 1

    for n in bucket:
        results *= n

    return results


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
