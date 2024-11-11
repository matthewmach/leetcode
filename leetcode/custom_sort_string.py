"""
Solution:
- need to find all the elements in s shared in order
- idea
    - create dict with counter of characters in s
    - iterate though order checking if there are remaining characters left
    - add all missing characters at the end
"""

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        out = ""
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        
        for c in order:
            if c in s_dict and s_dict[c] > 0:
                for i in range(s_dict[c]):
                    out = out + c
                s_dict[c] = 0
        
        for key in s_dict:
            if s_dict[key] > 0:
                for i in range(s_dict[key]):
                    out = out + key
        
        return out