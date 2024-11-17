# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = [root.val]
        def helper(node):
            if node:
                if abs(node.val - target) == abs(closest[0] - target):
                    closest[0] = min(node.val, closest[0])
                elif abs(node.val - target) < abs(closest[0] - target):
                    closest[0] = node.val
                helper(node.left)
                helper(node.right)
        helper(root)

        return closest[0]