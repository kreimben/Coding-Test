"""
https://www.algoexpert.io/questions/min-max-stack-construction
Min Max Stack Construction
"""


# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []  # Ordering should be ascending

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def push(self, number):
        self.stack.append(number)

    def getMin(self):
        result = float('inf')
        for num in self.stack:
            if result > num:
                result = num
        return result

    def getMax(self):
        result = float('-inf')
        for num in self.stack:
            if result < num:
                result = num
        return result
