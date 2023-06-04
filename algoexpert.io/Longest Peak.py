"""
https://www.algoexpert.io/questions/longest-peak
Longest Peak
"""


def longestPeak(array: [int]):
    curr_peak, max_peak = 0, 0
    is_increasing = False
    is_decreasing = False
    for i in range(1, len(array)):
        prev_num = array[i - 1]
        curr_num = array[i]
        if curr_num > prev_num:
            is_increasing = True
            if is_decreasing is False:
                if curr_peak == 0:
                    curr_peak += 2
                else:
                    curr_peak += 1
            else:
                max_peak = max(curr_peak, max_peak)
                curr_peak = 2
                is_decreasing = False

        elif curr_num < prev_num:
            if curr_peak == 0:
                is_increasing, is_decreasing = False, False
                continue
            else:
                curr_peak += 1
                is_increasing, is_decreasing = False, True

        else:
            if is_decreasing is True:
                max_peak = max(curr_peak, max_peak)

            curr_peak = 0
            is_increasing, is_decreasing = False, False

    if is_decreasing is True:
        return max(curr_peak, max_peak)
    return max_peak


assert longestPeak([5, 4, 3, 2, 1, 2, 1]) == 3
assert longestPeak([1, 3, 2]) == 3
assert longestPeak([]) == 0
assert longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]) == 6
