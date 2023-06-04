"""
https://www.algoexpert.io/questions/underscorify-substring
Underscorify Substring
"""


def underscorifySubstring(string, substring):
    l = []

    for i, ch in enumerate(string):
        block = string[i: i + len(substring)]
        if block == substring:
            l.append((i, i + len(substring)))

    # After find all substring indices, Merge it if possible.
    # Sort by starting index.
    l.sort(key=lambda x: x[0])
    merged = []
    # [(0, 4), (14, 18), (18, 22), (33, 37), (36, 40), (39, 43)] => initial value
    while l:
        tstart, tend = l.pop(0)
        for _ in range(len(l)):
            dstart, dend = l[0]

            if tend >= dstart:  # Yes
                tstart = min(tstart, dstart)
                tend = max(tend, dend)
                l.pop(0)  # already used
            else:
                break

        merged.append((tstart, tend))

    for start, end in reversed(merged):
        string = string[:start] + '_' + string[start:end] + '_' + string[end:]
    return string


assert underscorifySubstring('abababababababababababababaababaaabbababaa',
                             'a') == '_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_aa_b_a_b_aaa_bb_a_b_a_b_aa_'
assert underscorifySubstring('tzttztttz', 'ttt') == 'tzttz_ttt_z'
assert underscorifySubstring("testthis is a testtest to see if testestest it works", 'test') == \
       '_test_this is a _testtest_ to see if _testestest_ it works'
