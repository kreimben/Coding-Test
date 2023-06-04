"""
https://leetcode.com/problems/trapping-rain-water/
Trapping Rain Water
"""


class Solution:
    def trap(self, height: [int]) -> int:
        """
        잘 생각 해보면 for문으로 각 level마다 돌아가며 앞뒤로 블록이 있는지 (양 끝 벽은 인정 안됨) 체크해 주고 있으면 count를 올려주면 된다.
        """
        count = 0

        for level in range(max(height)):
            # level은 각각의 층을 말하는 것임
            first_block_index = -1  # 초기값

            for index in range(len(height)):
                if height[index] > level:
                    if first_block_index == -1:
                        first_block_index = index
                    else:
                        # 처음에 블록이 있었던 곳과의 거리 계산을 해줘 count에 더한다.
                        if index - first_block_index > 1:
                            # 차이가 1밖에 안난다면 바로 옆에 블록이 있다는 뜻이니깐 더해주지 않는다.
                            count += index - first_block_index - 1
                        first_block_index = index

        return count


s = Solution()

print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # == 6)
print(s.trap([4, 2, 0, 3, 2, 5]))  # == 9)
"""
0 0 0 0 0 1
1 0 0 0 0 1
1 0 0 1 0 1
1 1 0 1 1 1
1 1 0 1 1 1
"""
