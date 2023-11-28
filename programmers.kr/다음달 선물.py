"""
다음달 선물
"""

from collections import defaultdict


def solution(friends: [str], gifts: [str]):
    # friends.sort()

    # taken -> 준 사람 -> len(graph['key']) 하면 자동으로 구해짐
    # given -> 받운 사람 -> 별도의 변수 만들어서 관리
    given = defaultdict(int)
    graph = defaultdict(list)  # directed_graph
    for gift in gifts:
        sender, t = gift.split()
        graph[sender].append(t)
        given[t] += 1

    maxval = 0

    for friend in friends:
        curr_max = 0
        for target in friends:
            if friend == target: continue
            A = graph[friend].count(target)
            B = graph[target].count(friend)
            if A == B:
                # 주고 받은 수가 같으니, 선물 지수로 비교
                friend_gift_score = len(graph[friend]) - given[friend]
                target_gift_score = len(graph[target]) - given[target]
                if friend_gift_score > target_gift_score:
                    curr_max += 1
            elif A > B:
                curr_max += 1
        maxval = max(maxval, curr_max)

    return maxval


assert solution(
    friends=['muzi', 'ryan', 'frodo', 'neo'],
    gifts=['muzi frodo', 'muzi frodo', 'ryan muzi', 'ryan muzi', 'ryan muzi', 'frodo muzi', 'frodo ryan', 'neo muzi']
) == 2
