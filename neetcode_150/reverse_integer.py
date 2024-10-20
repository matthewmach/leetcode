class Solution:
    def reverse(self, x: int) -> int:
        out = 0
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        while x > 0:
            digit = x % 10
            out = out * 10 + digit
            x = x // 10
        if out > 2 ** 31 -1 or out < -2 ** 31:
            return 0
        if neg:
            return -out
        return out 