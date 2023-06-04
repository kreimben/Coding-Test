"""
https://www.algoexpert.io/questions/class-photos
Class Photos
"""

"""
Every class have even number of students.
"""


def classPhotos(redShirtHeights: [int], blueShirtHeights: [int]):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    # First, I should compare which color is taller.
    if redShirtHeights[0] > blueShirtHeights[0]:
        # In this case, Every red shirts wearer is taller than blue shirts wearer.
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] < blueShirtHeights[i]:
                break
        else:
            # In this case, Everything is ok.
            return True
        return False

    elif redShirtHeights[0] < blueShirtHeights[0]:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] > blueShirtHeights[i]:
                break
        else:
            return True
        return False

    else:
        return False


assert classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]) == True
assert classPhotos([5, 6], [5, 4]) == True
assert classPhotos([4, 5], [5, 4]) == False
