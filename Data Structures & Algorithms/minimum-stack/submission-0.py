class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.length = 0
        self.min_len = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_len == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[self.min_len - 1], val))
        self.length += 1
        self.min_len += 1
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.length -= 1
        self.min_len -= 1

    def top(self) -> int:
        return self.stack[self.length - 1]

    def getMin(self) -> int:
        return self.min_stack[self.min_len - 1]
