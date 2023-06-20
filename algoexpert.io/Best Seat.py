"""
https://www.algoexpert.io/questions/best-seat
Best Seat
"""


def bestSeat(seats):
    # should return index of most appropriate seats
    candidates = {}  # key is total current seat counts. value is index.
    left, right = 1, 2
    while right < len(seats):
        while left >= right:
            right += 1

        if seats[left] != 0:
            left += 1
            continue

        if seats[right] != 1:
            right += 1
            continue

        if seats[left] == 0 and seats[right] == 1:
            curr_count = right - left
            if curr_count % 2 == 0:
                candidates[curr_count] = min((right + left) // 2 - 1, candidates.get(curr_count, float('inf')))
            else:
                candidates[curr_count] = min((right + left) // 2, candidates.get(curr_count, float('inf')))

        left = right
        right += 1

    if candidates.keys():
        keys = sorted(candidates.keys(), reverse=True)
        for key in keys:
            return candidates[key]
    else:
        return -1


assert bestSeat([1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1]) == 5
