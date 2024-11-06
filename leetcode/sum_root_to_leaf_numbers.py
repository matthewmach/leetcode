# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Solution:
- recursion, return number built
- can use dfs, review
"""

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, cur_num, root):
            if node == None:
                return 0
            
            cur_num = cur_num * 10 + node.val
            left = helper(node.left, cur_num, False)
            right = helper(node.right, cur_num, False)
            out = left + right
            if left == 0 and right == 0:
                out += cur_num
            return out
        out = helper(root, 0, True)
        return out 