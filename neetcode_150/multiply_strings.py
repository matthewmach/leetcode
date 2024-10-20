class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Idea: do long multiplication
        # Reverse digits and multiply one by one
        out = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for d1 in range(len(num1)):
            for d2 in range(len(num2)):
                s = int(num1[d1]) * int (num2[d2]) + out[d1 + d2]
                out[d1 + d2 + 1] += s // 10
                out[d1 + d2] = s % 10

        # find where the zeroes stop 
        end = 0
        while end < len(out) and out[-end-1] == 0:
            end += 1
        if end != 0:
            out = out[:-end]

        # Reverse the order again and build the output stirng
        res = ""
        for i in range(len(out)-1, -1, -1):
            res = res + str(out[i])
        return res