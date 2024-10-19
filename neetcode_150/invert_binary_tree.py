# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            newLeft = newRight = None
            if root.right:
                newLeft = self.invertTree(root.right)
            if root.left:
                newRight = self.invertTree(root.left)
            root.left = newLeft
            root.right = newRight
        return root

    def optimal(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root