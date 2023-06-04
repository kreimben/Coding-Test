"""
https://www.algoexpert.io/questions/sort-stack
Sort Stack
"""


def sortStack(stack):
    # Before we start to sort,
    # We have to fix what to pop, push, peek.
    # 1. Pop first. To check second top of stack.
    # 2. Peek first.
    # 3. Compare that popped value and peek value.
    # 4. If popped value is bigger, pop the stack until find value is smaller than first popped value.
    store = []
    first = stack.pop()
    while stack:
        top = stack[-1]
        if first < top:
            second = stack.pop()
            stack.append(first)
            stack.append(second)
            for ele in reversed(store):
                stack.append(ele)
            else:
                store = []
        else:
            store.append(first)

        first = stack.pop()
    else:
        store.append(first)
        for ele in reversed(store):
            stack.append(ele)

    return stack


assert sortStack([-5, 2, -2, 4, 3, 1]) == [-5, -2, 1, 2, 3, 4]
