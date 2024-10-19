# idea: bitshift to get each bit and shift it to it's reversed position
class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            bit = (n >> i) & 1
            out += (bit << (31-i))
        return out