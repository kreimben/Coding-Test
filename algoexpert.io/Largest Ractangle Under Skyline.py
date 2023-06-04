"""
https://www.algoexpert.io/questions/largest-rectangle-under-skyline
Largest Ractangle Under Skyline
"""


def largestRectangleUnderSkyline(buildings):
    min_height = min(buildings)
    max_height = max(buildings)

    max_area = 0

    for height in range(min_height, max_height + 1):
        # Find very first index of height
        last = len(buildings) - 1
        for i in range(len(buildings) - 1, -1, -1):
            if buildings[i] < height:
                last = i
        # Find very last index of height
        first = 0
        for i in range(len(buildings)):
            if buildings[i] < height:
                first = i

        mh = min(buildings[first:last + 1])
        area = mh * (last - first + 1)
        max_area = max(max_area, area)

    return max_area


assert largestRectangleUnderSkyline([10, 1, 2, 3, 3, 5, 6, 7]) == 15
assert largestRectangleUnderSkyline([25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
assert largestRectangleUnderSkyline([5]) == 5
assert largestRectangleUnderSkyline([1, 3, 3, 2, 4, 1, 5, 3, 2]) == 9
