class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) -1
        carry = 1
        while i > -1 and carry == 1:
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10
            i -= 1
        if carry == 1:
            digits = [1] + digits
        return digits