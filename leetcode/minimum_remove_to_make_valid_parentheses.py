class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l_loc, r_loc = [], []        
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                l_loc.append(i)
            elif c == ")":
                if l_loc:
                    l_loc.pop()
                else:
                    r_loc.append(i)

        loc = l_loc + r_loc
        loc = set(loc)
        out = ""
        
        for i in range(len(s)):
            if not i in loc:
                out = out + s[i]
        return out

    # Worse worst case but faster in practice
    def faster(self, s: str) -> str:
        l_loc, r_loc = [], []        
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                l_loc.append(i)
            elif c == ")":
                if l_loc:
                    l_loc.pop()
                else:
                    r_loc.append(i)

        loc = l_loc + r_loc
        loc.sort()
        out = ""
        prev = 0
        for i in loc:
            if prev != i:
                out = out + s[prev:i]
            prev = i+1
        if prev != len(s):
            out = out + s[prev:]
        return out
