"""
https://school.programmers.co.kr/learn/courses/30/lessons/64061
크레인 인형뽑기 게임
"""


def solution(board, moves):
    stack = []
    count = 0
    while moves:
        move = moves[0] - 1

        for line in board:
            if line[move]:
                stack.append(line[move])
                line[move] = 0
                if check_stack(stack):
                    stack.pop()
                    stack.pop()
                    count += 2
                break
        moves.pop(0)

    return count


def check_stack(arr: []) -> bool:
    if len(arr) < 2:
        return False

    if arr[len(arr) - 1] == arr[len(arr) - 2]:
        return True
    else:
        return False


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
assert solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]) == 4