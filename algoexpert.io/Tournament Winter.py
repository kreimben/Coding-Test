"""
https://www.algoexpert.io/questions/tournament-winner
Tournament Winter
"""
from collections import defaultdict


def tournamentWinner(competitions: [[str]], results: [int]) -> str:
    # 1 means 'home team won' and 0 means 'away team won'.
    # and then at least we don't need count the each scores.
    d = defaultdict(int)
    for i, comp in enumerate(competitions):
        if results[i]:
            won = comp[0]
        else:
            won = comp[1]

        d[won] += 1  # We don't need to add actual 3 points.

    return max(d, key=d.get)


assert tournamentWinner(
    [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ],
    [0, 0, 1]
) == 'Python'
