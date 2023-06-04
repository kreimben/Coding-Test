"""
신고 결과 받기
https://school.programmers.co.kr/learn/courses/30/lessons/92334
"""


def solution(id_list, reports, k):
    # Make chart.
    reported_chart = [[False for col in range(len(id_list))] for row in range(len(id_list))]

    # Display input values to chart.
    for report in reports:
        reporter = report.split(' ')[0]
        reportee = report.split(' ')[1]

        reporter_index = get_index_of_list(id_list, reporter)
        reportee_index = get_index_of_list(id_list, reportee)

        reported_chart[reporter_index][reportee_index] = True

    # Layer 1.
    l1 = [False for value in range(len(id_list))]
    for index in range(len(id_list)):
        for j in range(len(id_list)):
            l1[index] += reported_chart[j][index]
    # print(f'l1: {l1}')

    # Layer 2.
    l2 = []
    for index in range(len(id_list)):
        if l1[index] >= k:
            temp = []
            for j in range(len(id_list)):
                temp.append(reported_chart[j][index])
            l2.append(temp)
    #print(f'l2: {l2}')

    # Layer 3.
    l3 = [0 for _ in range(len(id_list))]
    for i in range(len(id_list)):
        for j in range(len(l2)):
            l3[i] += l2[j][i]
    print(l3)


def get_index_of_list(id_list, value):
    # No duplicated value in list.
    for index in range(len(id_list)):
        if id_list[index] == value:
            return index


# solution(id_list=["muzi", "frodo", "apeach", "neo"],
#          reports=["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
#          k=2)

solution(id_list=["con", "ryan"],
         reports=["ryan con", "ryan con", "ryan con", "ryan con"],
         k=3)
