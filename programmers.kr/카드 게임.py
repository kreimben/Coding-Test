"""
카드 게임
"""


def two_sum(target: int, nums: [int]) -> (int, int):
    for i, num in enumerate(nums):
        if target - num in nums:
            find = nums.index(target - num)
            return (nums[find], num) if nums[find] < num else (num, nums[find])
    return None, None


def solution(coin: int, cards: [int]):
    # 맨 처음에 n/3개를 가짐.
    N = len(cards)
    initial_amount = N // 3

    have = []
    for _ in range(initial_amount):
        have.append(cards.pop(0))

    round = 1
    target = N + 1
    while coin >= 0 and cards:
        temp = []
        while len(temp) < 2 and cards:
            temp.append(cards.pop(0))
        # two sum
        one, two = two_sum(target, have + temp)
        if one is None and two is None:
            return round
        else:
            if one in temp:
                if coin > 0:
                    coin -= 1
                    temp.remove(one)
                    have.append(one)
                else:
                    return round
            if two in temp:
                if coin > 0:
                    coin -= 1
                    temp.remove(two)
                    have.append(two)
                else:
                    return round

            have += temp

            if one in have:
                have.remove(one)
            if two in have:
                have.remove(two)

        round += 1

    return round


assert solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]) == 5
