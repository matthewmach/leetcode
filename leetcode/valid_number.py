"""
Solution:
- split by e and lower
- check for - or + sign
- check for empty decimal and exponent
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        exp = s.split("e")
        if len(exp) > 2:
            return False

        if len(exp[0]) > 0 and exp[0][0] in {"-", "+"}:
            exp[0] = exp[0][1::]

        out = True
        dec = exp[0].split(".")
        if len(dec) == 2:
            if not dec[0]:
                out = out and dec[1].isnumeric()
            elif not dec[1]:
                out = out and dec[0].isnumeric()
            else:
                out = out and dec[0].isnumeric() and dec[1].isnumeric()
        elif len(dec) == 1:
            out = out and dec[0].isnumeric()
        else:
            return False
        
        if len(exp) == 2:
            if len(exp[1]) > 0 and exp[1][0] in {"-", "+"}:
               exp[1] = exp[1][1::]
            return out and exp[1].isnumeric()

        return out