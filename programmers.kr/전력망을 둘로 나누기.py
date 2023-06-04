"""
https://school.programmers.co.kr/learn/courses/30/lessons/86971
전력망을 둘로 나누기
"""


def find_diff(wires: [[int]]) -> int:
    # [[1,3],[2,3] ||| [4,5],[4,6],[4,7],[7,8],[7,9]]
    left, right = {wires[0][0]}, set()

    w = wires.copy()

    while w:
        wi = w.pop(0)

        # Find left first.
        if wi[0] in left or wi[1] in left:
            left.update([wi[0], wi[1]])
        elif wi[0] in right or wi[1] in right:
            right.update([wi[0], wi[1]])
        else:
            right.update([wi[0], wi[1]])

        # Find connected things.
        for e in left:
            if e in right:
                left.update(right)
                right = set()
                break

    if len(left) == 0:
        # 위의 코드를 살펴 볼때 left가 0이면 right역시 0일 가능성이 높고, 이 뜻은 함수가 받은 wires 빈 array라는 뜻이다.
        return 0
    elif len(right) == 0:
        # 이런 경우는 left에만 꽉차고 right에는 아무것도 없는 것이다.
        # 왜 한개를 빼주냐면, 이미 이 함수에 들어온 wires는 무조건 2개로 나뉘는 트리구조 일텐데,
        # right이 0이라는 것은 실제로 그려볼때 딱 하나의 송전탑만 끊켜 있다는 뜻이다.
        return len(left) - 1
    else:
        return abs(len(left) - len(right))


def solution(n: int, wires: [[int]]):
    # wire 정렬. 앞의 숫자를 기준으로 정렬
    wires = sorted(wires, key=lambda x: (x[0], x[1]))

    # 1. 모든 송전탑은 트리 형태로 반드시 "연결" 되어있다.
    # 2. 모든 네트워크는 반드시 "2개"로 나누어야 한다.
    # 3. 나눈 2개의 네트워크에 있는 송전탑의 갯수 차이는 가장 적어야 (minimum) 한다.
    # 4. 2개로 나누는 방법은 wires에 있는 연결관계들 중 하나"만" 끊어야 한다.
    # 5. 하나의 송신탑은 무조건 다른 "하나"의 송신탑과 연결 되어있다.
    # 6. 한개씩 빠진 wires를 입력받는 함수를 만들고 그 함수가 해당 숫자들을 주위로 몇개의 송전탑이 있는지 구하게 만든다.
    results = []
    for wire in wires:  # 0~7 8개
        results.append(
            find_diff(
                list(filter(lambda x: x != wire, wires))
            )
        )  # i번째 요소 빼서 함수에 집어넣음.

    return min(results)


assert solution(9, [[2, 3], [3, 4], [4, 5], [4, 7], [7, 8], [7, 9], [1, 3], [4, 6]]) == 3
assert solution(4, [[1, 2], [2, 3], [3, 4]]) == 0
assert solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]) == 1
