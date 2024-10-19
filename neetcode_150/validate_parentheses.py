class Solution:
    # Time Complexity: O(n)
    # Space Complexity: worst case O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if len(stack) > 0 and ((stack[-1] == '[' and c == ']') or (stack [-1] == '(' and c == ')') or (stack[-1] == '{' and c == '}')):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
    
    def optimal(self, s: str) -> bool:
        dic = {")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            if c in dic:
                if not stack or stack[-1] != dic[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack