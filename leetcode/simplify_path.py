"""
Input: String representing an absolute path
Output: Simplified canonical path

Solution:
- Make a stack adding directories/file names as you go
- For single period, ignore
- For double period, remove the last element 


- Note!!!: python split on / will just have empty elements
"""


class Solution:
    def initial(self, path: str) -> str:
        stack = []
        i = 0
        cur_str = ""

        def add_to_stack():
            if cur_str != ".":
                if cur_str == "..":
                    if len(stack) > 0:
                        del stack[-1]
                elif cur_str != "":
                    stack.append(cur_str)

        while i < len(path):
            c = path[i]
            if c == "/":
                while i < len(path) and path[i] == "/":
                    i += 1
                add_to_stack()
                cur_str = ""
            else:
                cur_str = cur_str + c
                i = i + 1

        add_to_stack()
        return "/" + "/".join(stack)

    def simplifyPath(self, path: str) -> str:
        filepath = []
        abs_path = path.split("/")
        
        for f in abs_path:
            if filepath and f == "..":
                filepath.pop()
            elif f not in [".", "..", ""]:
                filepath.append(f)
        
        return "/" + "/".join(filepath)
        