# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Input: bst, low, high
Output: sum of nodes with values [low, high]

sol:
- recursively go through tree
    - if val < high, recurse right
    - if val > low, recurse left
    - add if value in range
- dfs
"""
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(node):
            if not node:
                return 0
            
            out = 0
            if low <= node.val <= high:
                out += node.val
            
            if node.val > low:
                out += helper(node.left)
            if node.val < high:
                out += helper(node.right)

            return out
        
        return helper(root)