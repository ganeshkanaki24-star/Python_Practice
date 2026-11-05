# 32. Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1).

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):

        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):

        if not self.stack:
            return None

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self):

        if not self.stack:
            return None

        return self.stack[-1]

    def getMin(self):

        if not self.min_stack:
            return None

        return self.min_stack[-1]


stack = MinStack()

stack.push(10)
stack.push(5)
stack.push(20)

print("Top:", stack.top())
print("Minimum:", stack.getMin())

stack.pop()

print("Minimum after pop:", stack.getMin())