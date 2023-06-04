"""
https://www.algoexpert.io/questions/task-assignment
Task Assignment
"""


def taskAssignment(k: int, tasks: [int]):
    sorted_tasks = sorted(list(enumerate(tasks)), key=lambda x: x[1])
    results = []

    # [1, 1, 3, 3, 4, 5]
    # 1 and 5 => [0, 2]
    # 1 and 4 => [4, 5]
    # 3 and 3 => [1, 3]
    for i in range(len(sorted_tasks) // 2):
        first_index, _ = sorted_tasks[i]
        second_index, _ = sorted_tasks[len(sorted_tasks) - 1 - i]
        results.append(
            [
                first_index,
                second_index
            ]
        )

    return results


print(f'{taskAssignment(3, [87, 65, 43, 32, 31, 320])=}')
print(f'{taskAssignment(5, [3, 7, 5, 4, 4, 3, 6, 8, 3, 3])=}')
print(f'{taskAssignment(3, [1, 3, 5, 3, 1, 4])=}')
