class MinStack:
    # Time Complexity: O(1) each operation
    # Space Complexity: O(n)

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:
        self.stack.append((val, self.minVal))
        if self.minVal == None or self.minVal > val:
            self.minVal = val

    def pop(self) -> None:
        self.minVal = self.stack[-1][1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minVal
