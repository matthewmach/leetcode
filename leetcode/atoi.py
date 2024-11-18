class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0

        negative = False
        if s[0] == "-":
            negative = True
            s = s[1::]
        elif s[0] == "+":
            s = s[1::]
        
        out = 0
        bound = 2147483648
        zeroes = 0
        while zeroes < len(s) and s[zeroes] == "0":
            zeroes += 1
        
        i = zeroes
        while i < len(s) and s[i].isnumeric():
            if i > zeroes + 11:
                break
            out = out * 10 + int(s[i])
            i += 1

        if negative:
            return max(-out, -bound)
        else:
            return min(out, bound-1) 