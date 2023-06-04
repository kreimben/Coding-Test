"""
https://school.programmers.co.kr/learn/courses/30/lessons/12924
숫자의 표현
"""


def solution(n):
    """
    1부터 1+2+3+4...등 더함으로써 가능한 케이스인지 구한다.
    만약 1이 안될 경우 2로 넘어가서 2+3+4+5...등이 가능한지 구한다.
    """

    start_num = 1
    possible = 0

    while start_num < n:  # 1 부터 계속해서 키워감. n보다 적을 때 까지만 증가
        check_num = 0  # 임시로 저장해 두는 곳
        for number in range(start_num, n):
            check_num += number
            if check_num == n:
                possible += 1
                break
            elif check_num > n:
                break

        start_num += 1

    possible += 1
    return possible


print(solution(15))
