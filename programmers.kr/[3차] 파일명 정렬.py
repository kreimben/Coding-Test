"""
https://school.programmers.co.kr/learn/courses/30/lessons/17686
[3차] 파일명 정렬
"""


def is_number(ch: str) -> bool:
    d = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    if len(ch) == 1 and ch in d:
        return True
    else:
        return False


class File:
    def __init__(self, file_name: str, index: int):
        self.head = ''
        self.number = ''
        self.original = file_name
        self.original_index = index

    def evaluate(self):
        end_number = False
        for ch in self.original:
            if not is_number(ch):
                if end_number:
                    break
                self.head += ch
            elif len(self.number) < 6:
                self.number += ch
                end_number = True
            else:
                break
        # print(f'{self.head}{self.number}')

    def __gt__(self, other):
        # first standard is head.
        if self.head.lower() != other.head.lower():
            return self.head > other.head

            # second standard is number.
        elif self.number != other.number:
            return int(self.number) > int(other.number)

        # third standard is original number
        else:
            return self.original_index > other.original_index

    def __repr__(self):
        return f'{self.original}'


def solution(files: [str]):
    """
    Head is just before the number.
    Number is the section where all character is number.
    Tail is just after the number.
    """
    f: [File] = []
    for index, file in enumerate(files):
        obj = File(file, index)
        obj.evaluate()
        f.append(obj)

    while True:
        count = 0

        for index, file_obj in enumerate(f):
            if index + 1 < len(f) and f[index] > f[index + 1]:
                f[index], f[index + 1] = f[index + 1], f[index]
                count += 1

        if count == 0:
            break

    return [file.__repr__() for file in f]


assert solution(["O49qcGPHuRLR5FEfoO00321", "O00321"]) == ["O49qcGPHuRLR5FEfoO00321", "O00321"]
assert solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]) == ["img1.png",
                                                                                                  "IMG01.GIF",
                                                                                                  "img02.png",
                                                                                                  "img2.JPG",
                                                                                                  "img10.png",
                                                                                                  "img12.png"]
