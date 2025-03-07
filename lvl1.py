class StackWithMinMax:
    def __init__(self):
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Stack to store minimums
        self.max_stack = []  # Stack to store maximums

    def push(self, x):
        self.stack.append(x)
        # Push to the min_stack if it's empty or x is smaller than the current min
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        # Push to the max_stack if it's empty or x is larger than the current max
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if self.stack:
            popped_value = self.stack.pop()
            # If the popped value is the current min or max, pop from their respective stacks
            if popped_value == self.min_stack[-1]:
                self.min_stack.pop()
            if popped_value == self.max_stack[-1]:
                self.max_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

    def getMax(self):
        return self.max_stack[-1] if self.max_stack else None

# Usage Example
stack = StackWithMinMax()
stack.push(3)
stack.push(5)
stack.push(2)
print(stack.getMin())  # Output: 2
print(stack.getMax())  # Output: 5
stack.pop()
print(stack.getMin())  # Output: 3
print(stack.getMax())  # Output: 5
