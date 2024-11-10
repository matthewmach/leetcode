"""
Review Editorial
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = 0
        out = ""
        num1 = num1[::-1]
        num2 = num2[::-1]
        while i < len(num1) or i < len(num2):
            add = carry
            if i < len(num1):
                add += int(num1[i])
            if i < len(num2):
                add += int(num2[i])
            out = out + str(add % 10)
            carry  = add // 10
            i += 1
        if carry == 1:
            out = out + "1"
        return out[::-1]