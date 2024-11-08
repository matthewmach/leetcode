"""
Solution:
- first thought is to count the number of parenthesis and then subtract the two
- however, if they're facing away from either other but "cancel each other out" it doesn't work
- easiest solution is probably a stack
- only pop for righ side parenthesis

"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            print (stack)
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack)