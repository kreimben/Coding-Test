"""
https://school.programmers.co.kr/learn/courses/30/lessons/42578
위장
"""
from itertools import combinations


def solution(clothes: [[str]]):
    closet = {}
    numbers_of_combination = 0

    for item in clothes:
        kind = item[1]
        if closet.get(kind, None):
            closet[kind] += 1
        else:
            closet[kind] = 1

    # 첫째로 각 아이템에 대한 경우의 수를 곱해주면 된다.
    # 예를 들어 3번째 예제의 경우 headgear와 eyewear, face의 경우 각각 2개씩 존재한다.
    # 그렇다면 n개의 총 종류가 있다 가정했을 때, 1부터 n까지의 조합을 먼저 구해줘야 한다.
    for i in range(len(closet.keys()) + 1):
        data = list(combinations(closet.keys(), i))
        # 그 다음, 차례대로 조합 된 경우의 수를 곱해주면 된다.

        for comb in data:
            # 예를 들어, headgear와 eyewear 두가지 조합이 선택된다면,
            # 각각 2개씩 가지고 있으니 경우의 수는 4이다.
            # 여타 다른 조합들도 다들 마찬가지이니, 모두 합치면 12이다.
            # 조합이 3개씩 들어갈 경우 각각 2개씩 있는 아이템들이 3번씩 곱해지니깐 2의 3제곱, 즉 8이 된다.
            t = 1
            for k in comb:
                t *= closet[k]
            numbers_of_combination += t
            # 따라서 최종 정답을 20을 더한 26이 된다.

    return numbers_of_combination - 1  # 안입은 경우의 수 하나를 빼준다.


assert(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5)
assert(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]) == 3)
assert(
    solution([["a", "headgear"], ["b", "headgear"], ["c", "eyewear"], ["d", "eyewear"], ["e", "face"], ["f", "face"]])\
    == 26)
