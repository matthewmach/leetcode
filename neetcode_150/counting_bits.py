# Idea: for every new digit added 2^n, we just add 1 to every previous value
class Solution:
    def countBits(self, n: int) -> List[int]:
        array = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            array[i] = 1 + array[i-offset]
        return array