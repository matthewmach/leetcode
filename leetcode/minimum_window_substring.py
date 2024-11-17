"""
Solution:
- two pointers for the window
- have dict of chars in the window
- have stack of elements
    - if element in stack already, can remove until the next element in the stack
- keep counter of elements that you have
- optimal solution
    - have a dict of the window and the required string
    - have a variable to increment if you get an equivalent number of elements in t
    - once the number is equal to the length of the dict, decrease the window until you can't no more
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        Tdic, window = defaultdict(int), defaultdict(int)
        for c in t:
            Tdic[c] += 1
        
        have, need = 0, len(Tdic)
        out = [-1, -1]
        outLen = float("infinity")
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in Tdic and window[c] == Tdic[c]:
                have += 1
            
            while have == need:
                if  outLen > r - l + 1:
                    outLen = r - l + 1
                    out = [l, r]
                window[s[l]] -= 1
                if s[l] in Tdic and window[s[l]] < Tdic[s[l]]:
                    have -= 1
                l += 1

        return s[out[0] : out[1] + 1] if outLen != float("infinity") else ""