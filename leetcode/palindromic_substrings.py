"""
- every individual character is a palindrome
- recursion with memotization?
    - what's the point of memotization in this, no point
- either add next character or have a single character string
- expand around possible centers
    - each character is a possible center
        - try to expand from each one
        - account for even and odd palindromes
        - this is n^2
"""

def countSubstrings(self, s: str) -> int:
    out = 0
    def expand_odd(center: int, size: int) -> int:
        if center - size >= 0 and center + size < len(s):
            if s[center - size] == s[center + size]:
                return expand_odd(center, size+1) + 1
        return 0
    def expand_even(r: int, l: int):
        if r >= 0 and l < len(s):
            if s[r] == s[l]:
                return expand_even(r-1, l+1) + 1
        return 0

    for i in range(len(s)):
        out += expand_odd(i, 0)
        if i < len(s) -1:
            out += expand_even(i, i+1)
    return out