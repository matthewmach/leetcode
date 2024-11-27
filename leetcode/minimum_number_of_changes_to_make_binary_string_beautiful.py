"""
keep track of current even substring and if it's constant 0 or 1s
- if it's not, start new and check
    - if you have 10/01, put in variable state
    - commit when next substring is 00/11
    - if not you can change

- note substring have to be even, so every 2*i, 2*i+1 pair is always stuck together
    - these pairs are considered substrings
    - it actually doesn't matter what it's surroundings are, just check every pair
"""

class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        out = 0
        while 2*i + 1 < len(s):
            if s[2*i] != s[2*i+1]:
                out += 1
            i += 1
        return out