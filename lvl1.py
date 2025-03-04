class CustomStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.maxStack = []

    def push(self, x: int):
        self.stack.append(x)
        
        # Maintain the minStack: if minStack is empty or x is smaller than or equal to the current minimum, push x.
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])
        
        # Maintain the maxStack: if maxStack is empty or x is greater than or equal to the current maximum, push x.
        if not self.maxStack or x >= self.maxStack[-1]:
            self.maxStack.append(x)
        else:
            self.maxStack.append(self.maxStack[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
            self.maxStack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.minStack[-1] if self.minStack else None

    def getMax(self):
        return self.maxStack[-1] if self.maxStack else None
