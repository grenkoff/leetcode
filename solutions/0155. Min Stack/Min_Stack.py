class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Time: O(1)
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # Time: O(1)
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Time: O(1)
        return self.stack[-1]

    def getMin(self) -> int:
        # Time: O(1)
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
