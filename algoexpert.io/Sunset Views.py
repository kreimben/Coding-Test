"""
https://www.algoexpert.io/questions/sunset-views
Sunset Views
"""


def sunsetViews(buildings, direction):
    """
    Take a maximum value's index.
    If west, right values from maximum value is meaningless.
    If east, left values from maximum value is meaningless.
    """
    if len(buildings) == 0: return []
    maxmimum_index = buildings.index(max(buildings))

    stamp = {}
    results = [maxmimum_index]
    prev = -1
    if direction == 'EAST':
        # Start from far east, (end to maxmimum value)
        for i in range(len(buildings) - 1, maxmimum_index, -1):
            height = buildings[i]
            if prev < height and not stamp.get(height):
                # First and only building to see sunset!
                results.append(i)
                stamp[height] = 1
                prev = height
    else:
        # Start from far west, (start to maximum value)
        for i in range(maxmimum_index):
            height = buildings[i]
            if prev < height and not stamp.get(height):
                results.append(i)
                stamp[height] = 1
                prev = height

    if len(results) == 1 and results[0] == -1:
        return []
    else:
        return sorted(results)


assert sunsetViews([1, 2, 3, 4, 5, 6], 'EAST') == [5]
assert sunsetViews([], 'EAST') == []
assert sunsetViews([1, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8], 'WEST') == [0, 1, 2, 4, 5, 6, 10, 13]
