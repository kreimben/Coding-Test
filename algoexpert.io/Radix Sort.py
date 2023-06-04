"""
https://www.algoexpert.io/questions/radix-sort
Radix Sort
"""


def radixSort(array):
    def init_q():
        q = [0] * 10
        for i in range(10):
            q[i] = []
        return q

    q = init_q()

    max_radix = len(str(max(array)))  # 8762 => max_radix == 4

    array = [
        str(ele) if len(str(ele)) == max_radix else '0' * (max_radix - len(str(ele))) + str(ele)
        for ele in array
    ]

    radix = max_radix

    while radix > 0:
        for element in array:
            r = str(element)[radix - 1]
            q[int(r)].append(element)
            q[int(r)].sort()

        temp = []
        for i in range(10):
            temp += q[i]
        array = temp
        radix -= 1
        q = init_q()

    return [int(ele) for ele in reversed(array)]


radixSort([8762, 654, 3008, 345, 87, 65, 234, 12, 2])
