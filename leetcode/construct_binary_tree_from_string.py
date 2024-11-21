# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Solution:
- recursively pass in the string contained within brackets
- split by (, need to explicitly split yourself 
    - remove ) from end
    - if 1 element, only left child
    - if 2 elements, then construct left and right
        - can () exist?
        - shouldn't matter just filter out empty strings
    - own split method is more liek ologn
"""

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def split_brackets(string: str) -> List[str]:
            left_count = 0
            cur = ""
            out = []
            i = 0
            while i < len(string) and string[i] != "(":
                cur = cur + string[i]
                i += 1
            out.append(cur)
            cur = ""

            for c in string[i:]:
                if c == "(":
                    left_count += 1
                elif c == ")":
                    left_count -= 1
                cur = cur + c
                if left_count == 0:
                   out.append(cur)
                   cur = ""
            return out 

        if not s:
            return None
        leaves = split_brackets(s)
        left, right = None, None
        if len(leaves) > 1:
            left = self.str2tree(leaves[1][1:-1])
        if len(leaves) > 2:
            right = self.str2tree(leaves[2][1:-1])
        
        val = 0
        if leaves[0][0] == "-":
            val = -int(leaves[0][1:])
        else:
            val = int(leaves[0])
        parent = TreeNode(val = val, left = left, right = right)
        return parent

    def optimized(self, s: str) -> Optional[TreeNode]:
        def get_val(s: str, index: int) -> Tuple[int, int]:
            cur = ""
            while index < len(s) and s[index] != "(" and s[index] != ")":
                cur = cur + s[index]
                index += 1
            if cur[0] == "-":
                return -int(cur[1:]), index
            return int(cur), index

        def helper(s: str, index: int) -> Tuple[Optional[TreeNode], int]:
            if index == len(s):
                return None, index

            val, index = get_val(s, index)
            node = TreeNode(val)
            if index < len(s) and s[index] == "(":
                node.left, index = helper(s, index+1)
            
            if node.left and index < len(s) and s[index] == "(":
                node.right, index = helper(s, index+1)
            
            if index < len(s) and s[index] == ")":
                index += 1
            return node, index

        return helper(s, 0)[0]
