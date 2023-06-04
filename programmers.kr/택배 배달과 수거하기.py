"""
https://school.programmers.co.kr/learn/courses/30/lessons/150369
택배 배달과 수거하기
"""


def solution(cap: int, n: int, deliveries: [int], pickups: [int]):
    total = 0

    while True:
        # If every element is 0, break the loop!
        for v in deliveries:
            if v != 0:
                break
        else:
            for v in pickups:
                if v != 0:
                    break
            else:
                break

        # Delivery first!
        delivery_max_distance = 0
        ncap = cap
        for i, v in enumerate(reversed(deliveries)):
            if ncap <= 0:
                break

            index = n - i - 1
            if v != 0:
                if delivery_max_distance == 0:
                    delivery_max_distance = index + 1

                if v > ncap:
                    deliveries[index] -= ncap
                    ncap = 0
                else:
                    deliveries[index] = 0
                    ncap -= v

        # And then pickup!
        pickup_max_distance = 0
        for i, v in enumerate(reversed(pickups)):
            index = n - i - 1
            if v != 0 and index <= delivery_max_distance and cap > ncap:
                margin = cap - ncap
                if pickup_max_distance == 0:
                    pickup_max_distance = index + 1 if delivery_max_distance == 0 else delivery_max_distance

                if margin >= pickups[index]:
                    pickups[index] = 0
                    ncap += v
                else:
                    pickups[index] -= margin
                    ncap = cap

        total += delivery_max_distance + pickup_max_distance

    return total


assert solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]) == 16
assert solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]) == 30
