class Solution:
    # adder implementation lol
    def adder(self, a: int, b: int) -> int:
        def adder (bit1, bit2, carry):
            xor = bit1 ^ bit2
            return [xor ^ carry, (bit1 & bit2) | (xor & carry) ]

        i = 0
        carry = 0
        out = 0
        while (a >> i) != 0 or (b >> i) != 0:
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1        
            add_out, carry = adder(a_bit, b_bit, carry)
            out = (add_out << i) ^ out
            i += 1
        if carry != 0:
            out = (carry << i) ^ out
        return out

    def getSum(self, a: int, b: int) -> int:
        def add(a,b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)
        
        if a * b < 0:
            if a > 0:
                return self.getSum(b,a)
            if add(~a, 1) == b:
                return 0
            if add(~a, 1) < b:
                return add(~add(add(~a, 1), add(~b, 1)), 1)

        return add(a,b)