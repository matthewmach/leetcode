class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.d = deque([])
        self.s = 0

    def next(self, val: int) -> float:
        if len(self.d) < self.size:
            self.d.append(val)
            self.s += val
        else:
            old = self.d.popleft()
            self.d.append(val)
            self.s += val - old
        return self.s / len(self.d)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)