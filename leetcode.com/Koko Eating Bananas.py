"""
https://leetcode.com/problems/koko-eating-bananas/
Koko Eating Bananas
"""
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: [int], h: int) -> int:
        """
        이진 탐색 트리로 문제를 풀면 된다.
        Brute-Force (그냥 무지성 0부터 푸는 방법)는 누가봐도 시간 효율성이 나오지 못함으로 패스.
        주어진 자료구조가 배열일때 이진 탐색 트리의 경우 left 좌표(인덱스)와 right 좌표를 설정해주고
        loop안에서 조건에 따라 left와 right를 조정해 가면서 풀어주면 된다. (괜히 다른 방법으로 풀면 시간 초과 뜬다)
        left 값은 1이나 0부터 시작할 필요가 없다.
        상식적으로 3, 6, 7, 11의 piles가 있다 가정할때 쉬는 시간 없이 고릴라가 먹을 수 있는 시간당 바바나의 갯수는
        (3+6+7+11)/(총 시간=h=8)=> 3.375개이다. 따라서 올림 처리를 하면 4개이고, 이것이 left좌표(시간당 4개 섭취)가 된다.
        이보다 적은 시간을 정하는 것은 의미가 없는것이다.
        right 값은 그냥 piles안에 있는 최대 값을 넣으면 된다.
        이렇게 left와 right이 정해졌으면 loop를 돌면서 조건에 맞게 구해주면된다.
        """
        left, right = ceil(sum(piles) / h), max(piles)
        result = right
        while left <= right:
            target = (left + right) // 2  # target은 무조건 left와 right의 중간 값
            time_spent = 0
            for col in piles:
                time_spent += ceil(col / target)

            # 걸린 시간(`time_spent`)이 h보다 많다는 것은 시간당 더 많은 바나나를 먹을 필요가 있다는 뜻이고,
            # 그 말은 탐색을 하는 범위의 최솟값을 증가 시켜야 한다는 말과 같다.
            if time_spent > h:
                left = target + 1
            else:
                # 만약에 걸린 시간(`time_spent`)이 h보다 적다면, right을 줄여 시간당 더 적은 바나나를 먹을 필요가 있다는 뜻이다.
                # 이 때의 target만이 result에 들어갈 수 있는데, 이유는 `time_spent <= h`가 True일때 적절한 후보가 될 수 있기 때문이다.
                result = target
                right = target - 1

            # 그렇게 해서 left와 right이 같아 지는 지점이 있을 것이다.
            # 그러면 그 직전에 구한 target이 답이 된다.
        return result


s = Solution()

assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
