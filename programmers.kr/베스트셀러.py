"""
https://github.com/Team-Discipline/Coding-Test/issues/67
베스트셀러
"""


def solution():
    n: int = int(input())
    books = {}
    for _ in range(n):
        new_book = input()
        if new_book in books.keys():
            books[new_book] += 1
        else:
            books[new_book] = 1
    return max(books, key=books.get)


print(solution())
