"""
https://www.algoexpert.io/questions/min-rewards
Min Rewards
"""


def minRewards(scores):
    rewards = [1] * len(scores)
    peaks = []
    valleys = []

    # What is peak?
    # Ascending through,
    # and got descending ever.
    ascending = None
    for i in range(len(scores) - 1):
        if scores[i] < scores[i + 1]:
            if not ascending or ascending is None:
                valleys.append(i)
            ascending = True
        elif scores[i] > scores[i + 1]:  # I can just simply use else but i want to exciplit the condition.
            if ascending or ascending is None:
                peaks.append(i)
            ascending = False

    if scores[len(scores) - 2] > scores[len(scores) - 1]:
        # reward of last position should be 1 So it is one of the valleys.
        valleys.append(len(scores) - 1)
    else:
        peaks.append(len(scores) - 1)

    # I have to merge with section.
    sections = []
    p = peaks.copy()
    v = valleys.copy()
    while p and v:
        peak = p[0] if p else None
        valley = v[0] if v else None
        if peak > valley:
            sections.append(
                [[valley, peak], 'A']
            )
            v.pop(0)
        else:
            sections.append(
                [[peak, valley], 'D']
            )
            p.pop(0)

    # To set reward as 1, I should find first valleys.
    for indices, order in sections:  # section [[[0, 3], 'D'], [[3, 7], 'A'], [[7, 8], 'D']]
        if order == 'A':
            level = 1  # rewards[indices[0]]
            for i in range(indices[0], indices[1] + 1):
                if rewards[i] == 1:
                    rewards[i] = level
                level += 1
        elif order == 'D':
            level = 1  # rewards[indices[0]]
            for i in range(indices[1], indices[0] - 1, -1):
                if rewards[i] < level:
                    rewards[i] = level
                level += 1

    return sum(rewards)


assert minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]) == 25
assert minRewards([0, 4, 2, 1, 3]) == 9
assert minRewards([5, 10]) == 3
assert minRewards([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 15
